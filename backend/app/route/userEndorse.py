from flask import request, Blueprint
from flask_jwt_extended import (
    jwt_required, 
    get_jwt_identity
)
from collections import namedtuple
from ..controller import userEndorse
from ..util.warpResponse import warpResponse, response
from ..util.logger import get_logger as log
from ..util.dataWarp import jsonWarp

bUserEndorse = Blueprint('userEndorse', __name__)

userEndorseFields = {"userGlobalID", "endorseBy", "endorseID", 'score'}

@bUserEndorse.route('/self', methods=['GET'])
@jwt_required
def findOneEndorse():
    jwtUserID = get_jwt_identity()

    result, code = userEndorse.Findone(jwtUserID)

    if code == 200:
        return warpResponse(response.OK, result)
    elif code == 404:
        return warpResponse(response.ResourceNotFound)

@bUserEndorse.route('/', methods=['POST'])
@jwt_required
def findAllEndorse():
    findUserEndorse = jsonWarp(request.get_json(), userEndorseFields, "findAllEndorse")

    result, code = userEndorse.Findall(
        userGlobalID=findUserEndorse.userGlobalID,
        endorseBy=findUserEndorse.endorseBy,
        score=findUserEndorse.score,
        endorseID=findUserEndorse.endorseID
        )

    if code == 200:
        return warpResponse(response.OK, result)
    elif code == 404:
        return warpResponse(response.ResourceNotFound)

@bUserEndorse.route('/add', methods=['POST'])
@jwt_required
def createNewUserEndorse():
    createUserEndorse = jsonWarp(request.get_json(), userEndorseFields, "createEndorse")
    jwtUserID = get_jwt_identity()

    code = userEndorse.Create(
        userGlobalID=createUserEndorse.userGlobalID,
        endorseBy=jwtUserID,
        score=createUserEndorse.score,
        endorseID=createUserEndorse.endorseID
        )

    if code == 200:
        return warpResponse(response.OK)
    elif code == 500:
        return warpResponse(response.NotImplemented)
    elif code == 409:
        return warpResponse(response.Conflit)

@bUserEndorse.route('/patch', methods=['POST'])
@jwt_required
def patchUserEndorse():
    patchUserEndorse = jsonWarp(request.get_json(), userEndorseFields, "patchEndorse")

    jwtUserID = get_jwt_identity()

    code = userEndorse.Patch(
        userGlobalID=patchUserEndorse.userGlobalID,
        endorseBy=jwtUserID,
        score=patchUserEndorse.score,
        endorseID=patchUserEndorse.endorseID
    )

    if code == 200:
        return warpResponse(response.OK)
    elif code == 500:
        return warpResponse(response.NotImplemented)
    elif code == 404:
        return warpResponse(response.ResourceNotFound)

@bUserEndorse.route('/delete', methods=['POST'])
@jwt_required
def deleteUserEndorse():
    deleteUserEndorse = jsonWarp(request.get_json(), userEndorseFields, "deleteEndorse")

    jwtUserID = get_jwt_identity()

    code = userEndorse.Delete(endorseBy=jwtUserID, endorseID=deleteUserEndorse.endorseID, userGlobalID=deleteUserEndorse.userGlobalID)

    if code == 200:
        return warpResponse(response.OK)
    elif code == 404:
        return warpResponse(response.ResourceNotFound)
    elif code == 500:
        return warpResponse(response.NotImplemented)


    