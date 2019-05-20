from flask import request, Blueprint
from flask_jwt_extended import (
    jwt_required, 
    get_jwt_identity
)
from collections import namedtuple
from ..controller import commentEndorse
from ..util.warpResponse import warpResponse, response
from ..util.logger import get_logger as log
from ..util.dataWarp import jsonWarp

bCommentEndorse = Blueprint('commentEndorse', __name__)

commentEndorseField = {"commentID", "endorseBy", "score"}

@bCommentEndorse.route('/one', methods=['POST'])
@jwt_required
def findOneCommentEndorse():
    commentEndorses = jsonWarp(request.get_json(), commentEndorseField, "findOneCommentEndorse")

    result, code = commentEndorse.Findall(commentID=commentEndorses.commentID)

    if code == 200:
        return warpResponse(response.OK, result)
    elif code == 404:
        return warpResponse(response.ResourceNotFound)

@bCommentEndorse.route('/self', methods=['GET'])
@jwt_required
def findAllCommentEndorse():
    result, code = commentEndorse.Findall(endorseBy=get_jwt_identity())

    if code == 200:
        return warpResponse(response.OK, result)
    elif code == 404:
        return warpResponse(response.ResourceNotFound)

@bCommentEndorse.route('/add', methods=['POST'])
@jwt_required
def createNewCommentEndorse():
    createCommentEndorse = jsonWarp(request.get_json(), commentEndorseField, "createCommentEndorse")
    jwtUser = get_jwt_identity()
    

    code = commentEndorse.Create(
        commentID=createCommentEndorse.commentID,
        endorseBy=jwtUser,
        score=createCommentEndorse.score
        )

    if code == 200:
        return warpResponse(response.OK)
    elif code == 500:
        return warpResponse(response.NotImplemented)

@bCommentEndorse.route('/patch', methods=['POST'])
@jwt_required
def patchCommentEndorse():
    patchCommentEndorse = jsonWarp(request.get_json(), commentEndorseField, "patchCommentEndorse")
    jwtUser = get_jwt_identity()

    code = commentEndorse.Patch(
        commentID=patchCommentEndorse.commentID,
        endorseBy=jwtUser,
        score=patchCommentEndorse.score
    )

    if code == 200:
        return warpResponse(response.OK)
    elif code == 500:
        return warpResponse(response.NotImplemented)
    elif code == 404:
        return warpResponse(response.ResourceNotFound)

@bCommentEndorse.route('/delete', methods=['POST'])
@jwt_required
def deleteCommentEndorse():
    deleteCommentEndorse = jsonWarp(request.get_json(), commentEndorseField, "deleteCommentEndorse")
    jwtUserID = get_jwt_identity()
    code = commentEndorse.Delete(commentID=deleteCommentEndorse.commentID, jwtUserID=jwtUserID)

    if code == 200:
        return warpResponse(response.OK)
    elif code == 404:
        return warpResponse(response.ResourceNotFound)
    elif code == 500:
        return warpResponse(response.NotImplemented)

