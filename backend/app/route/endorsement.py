from flask import request, Blueprint
from ..util.dataWarp import jsonWarp
from ..controller import endorsement
from ..util.warpResponse import warpResponse, response
from ..util.logger import get_logger as log

bEndorsement = Blueprint('endorsement', __name__)
endorsementField = {"name"}

@bEndorsement.route('/', methods=['POST'])
def findOneEndorse():
    newEndorse = jsonWarp(request.get_json(), endorsementField, "endorsement")
    log().debug(newEndorse.name)
    result, code = endorsement.Findone(name=newEndorse.name)

    if code == 200:
        return warpResponse(response.OK, result)
    elif code == 404:
        return warpResponse(response.ResourceNotFound)

@bEndorsement.route('/add', methods=['POST'])
def newEndorsement():
    newEndorse = jsonWarp(request.get_json(), endorsementField, "endorsement")

    code = endorsement.Create(newEndorse.name)
    
    if code == 200:
        return warpResponse(response.OK)
    elif code == 500:
        return warpResponse(response.ResourceNotFound)

@bEndorsement.route('/delete', methods=['POST'])
def deleteEndorse():
    delEndorse = jsonWarp(request.get_json(), endorsementField, "endorsement")
    code = endorsement.Delete(delEndorse.name)
    
    if code == 200:
        return warpResponse(response.OK)
    elif code == 500:
        return warpResponse(response.ResourceNotFound)
