from flask import Flask, jsonify
from .util.warpResponse import warpResponse, response
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate


from .config.conf import Config

from flask_cors import CORS

from .model import db
from app.model import user, emotionScore, keywords, comment, language, article


prefix = "/api"
def addPrefixToBlueprint(blueprintName, urlPrefix):
    global prefix
    app.register_blueprint(blueprintName,url_prefix=prefix + urlPrefix)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

flask_bcrypt = Bcrypt(app)



db.init_app(app)
migrate = Migrate(app, db)


from .route.article import barticle
CORS(app)

addPrefixToBlueprint(barticle, "/article")


@app.errorhandler(404)
def not_found(error):
    return warpResponse(response.ResourceNotFound)


@app.before_request
def befReq():
    db.session.rollback()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()