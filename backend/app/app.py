from flask import Flask, jsonify
from .util.warpResponse import warpResponse, response
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

from .config.conf import Config

from flask_cors import CORS

from .model import db
from app.model import userLogin, userEndorse, userProfile, comment, commentEndorse, endorsement


prefix = "/api"
def addPrefixToBlueprint(blueprintName, urlPrefix):
    global prefix
    app.register_blueprint(blueprintName,url_prefix=prefix + urlPrefix)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

flask_bcrypt = Bcrypt(app)

app.config['JWT_SECRET_KEY'] = Config.jwt_secret
jwt = JWTManager(app)

db.init_app(app)
migrate = Migrate(app, db)


from .route.userLogin import bUserLogin
from .route.comment import bComment
from .route.commentEndorse import bCommentEndorse
from .route.userEndorse import bUserEndorse
from .route.userProfile import bUserProfile
from .route.endorsement import bEndorsement

CORS(app)

addPrefixToBlueprint(bUserLogin, "/login")
addPrefixToBlueprint(bComment, "/comment")
addPrefixToBlueprint(bCommentEndorse, "/commentEndorse")
addPrefixToBlueprint(bUserEndorse, "/userEndorse")
addPrefixToBlueprint(bUserProfile, "/userProfile")
addPrefixToBlueprint(bEndorsement, "/endorsement")



@app.errorhandler(404)
def not_found(error):
    return warpResponse(response.ResourceNotFound)


@app.before_request
def befReq():
    db.session.rollback()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()