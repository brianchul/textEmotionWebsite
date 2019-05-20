from flask import jsonify
from .logger import get_logger as log
from .dataWarp import jsonWarp

messages = {
        "OK":               {'code':200, "message": "ok"},
        "ResourceNotFound": {'code':404, "message": "ResourceNotFound"},
        "InvalidArguments": {'code':400, "message": "InvalidArguments"},
        "WrongPassword":    {'code':401, "message": "Wrong Username or Password"},
        "UserExist":        {'code':409, "message": "User Exists"},
        "Conflit":          {'code':409, "message": "Parameter conflit"},
        "NoToken":          {'code':400, "message": "Token Required"},
        "ServerError":      {'code':500, "message": "There's an error occour."},
        "NotImplemented":   {'code':500, "message": "Request not implemented"},
        "Forbidden":        {'code':403, "message": "Forbidden"}
        }

response = jsonWarp(messages, list(messages), "warpResp")


def warpResponse(warpResp, data=None):
    if data is None:
       data = []
    return jsonify(data=data, response=warpResp)
