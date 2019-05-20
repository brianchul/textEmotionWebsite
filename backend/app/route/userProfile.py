from flask import request, Blueprint
from flask_jwt_extended import (
    jwt_required, 
    get_jwt_identity
)
from ..controller import userProfile
from ..util.warpResponse import warpResponse, response
from ..util.crawler import crawler
from ..util.logger import get_logger as log
from ..util.dataWarp import jsonWarp

bUserProfile = Blueprint('userProfile', __name__)

findTargetProfileFields = {'userGlobalID', 'userName', 'userURL'}
userProfileFields = {'userID', 'userGlobalID', 'userName', 'userURL', 'userMedia'}

@bUserProfile.route("/self", methods=['GET'])
@jwt_required
def findSelfProfile():
    userID = get_jwt_identity()
    query, code = userProfile.Findall(userID)

    if code == 200:
        return warpResponse(response.OK, query)
    elif code == 404:
        return warpResponse(response.ResourceNotFound)

@bUserProfile.route('/target', methods=['POST'])
@jwt_required
def findOrCreateTargetProfile():
    targetProfile = jsonWarp(request.get_json(), findTargetProfileFields, "findTargetProfile")
    if targetProfile.userURL is not None:
        query = userProfile.FindByURL(targetProfile.userURL)

        if query is not None:
            return warpResponse(response.OK, query)

        else:

            targetUserName, targetUserGlobalID = crawler(targetProfile.userURL)
            if targetUserGlobalID is None:
                return warpResponse(response.InvalidArguments)

            result = userProfile.Create(
                userName=targetUserName,
                userUrl=targetProfile.userURL,
                userGlobalID=targetUserGlobalID
                )

            if result == 200:
                query = userProfile.FindByURL(targetProfile.userURL)
                return warpResponse(response.OK, query)
            elif result == 409:
                return warpResponse(response.InvalidArguments)
            elif result == 500:
                return warpResponse(response.ServerError)
    else:
        return warpResponse(response.InvalidArguments)


@bUserProfile.route("/create", methods=['POST'])
@jwt_required
def createUserProfile():
    userProfiles = jsonWarp(request.get_json(), userProfileFields, 'newUserProfile')
    jwtUserID = get_jwt_identity()
    userGlobalID = None
    if userProfiles.userURL is not None:
        userGlobalID = crawler(userProfiles.userURL)

    code = userProfile.Create(
        userID=jwtUserID,
        userName=userProfiles.userName,
        userUrl=userProfiles.userURL,
        userMedia=userProfiles.userMedia,
        userGlobalID=userGlobalID
        )

    if code == 200:
        return warpResponse(response.OK)
    else:
        return warpResponse(response.ServerError)

@bUserProfile.route("/patch", methods=['POST'])
@jwt_required
def patchUserProfile():
    userProfiles = jsonWarp(request.get_json(), userProfileFields, 'patchUserProfile')
    jwtUserID = get_jwt_identity()

    result = userProfile.Patch(jwtUserID, userProfiles.userName, userProfiles.userURL, userProfiles.userMedia)

    if result == 200:
        return warpResponse(response.OK)
    elif result == 400:
        return warpResponse(response.ServerError)
    elif result == 404:
        return warpResponse(response.ResourceNotFound)

@bUserProfile.route('/delete', methods=['POST'])
@jwt_required
def deleteUserProfile():
    jwtUserID = get_jwt_identity()

    result = userProfile.Delete(jwtUserID)

    if result == 200:
        return warpResponse(response.OK)
    elif result == 404:
        return warpResponse(response.ResourceNotFound)