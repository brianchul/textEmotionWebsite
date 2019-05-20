from flask import request, Blueprint
from flask_jwt_extended import (
    jwt_required, 
    get_jwt_identity
)
from collections import namedtuple
from ..controller import userLogin
from ..util.warpResponse import warpResponse, response
from ..util.logger import get_logger as log
from ..util.facebook import facebookValid
from ..util.dataWarp import jsonWarp


bUserLogin = Blueprint('userLogin', __name__)

loginDataFields = {"loginProvider", "providerUserID", "providerUserName", "password", "token"}
createDataFields = {"loginProvider", "providerUserID", "providerUserName", "password", "userID"}

def validToken(token):
    fbData, isValid = facebookValid(token)
    if isValid:
        return fbData
    else:
        return None

@bUserLogin.route("/", methods=['POST'])
def loginOrCreate():
    request.get_json()['loginProvider'] = request.get_json()['loginProvider'].lower()
    loginUsers = jsonWarp(request.get_json(), loginDataFields, 'loginData')

    if loginUsers.token is not None:
        fbData = validToken(loginUsers.token)
        if fbData is None:
            return warpResponse(response.WrongPassword)
        loginUsers.providerUserID = fbData.user_id

    code, resp = userLogin.FindOne(
        loginUsers.loginProvider,
        loginUsers.providerUserID,
        loginUsers.providerUserName,
        loginUsers.password
        )

    if code == 400:
        return warpResponse(response.WrongPassword)
    elif code == 200:
        return warpResponse(response.OK, {'accessToken':resp})
    elif code == 404:
        if loginUsers.loginProvider == "facebook":
            # create user
            createUser = userLogin.Create(loginUsers.loginProvider, loginUsers.providerUserID, loginUsers.providerUserName, loginUsers.password)
            if createUser == 200:
                query = userLogin.FindOne(loginUsers.loginProvider, loginUsers.providerUserID, loginUsers.providerUserName, loginUsers.password)
                return warpResponse(response.OK, query)
            else:
                return warpResponse(response.ServerError)
        return warpResponse(response.WrongPassword)
        

@bUserLogin.route('/register', methods=['POST'])
def registerUser():
    createUsers = jsonWarp(request.get_json(), createDataFields, "createUser")

    isExists, _ = userLogin.FindOne(createUsers.loginProvider, createUsers.providerUserID, createUsers.providerUserName)
    log().debug(isExists)
    if isExists == 200:
        return warpResponse(response.UserExist)

    code = userLogin.Create(
        LoginProvider=createUsers.loginProvider.lower(),
        ProviderUserID=createUsers.providerUserID,
        ProviderUserName=createUsers.providerUserName,
        Password=createUsers.password
        )

    if code == 200:
        return warpResponse(response.OK)
    elif code == 400:
        return warpResponse(response.NotImplemented)

@bUserLogin.route('/testJwt', methods=['GET'])
@jwt_required
def testJWT():
    userID = get_jwt_identity()
    return warpResponse(response.OK, userID)