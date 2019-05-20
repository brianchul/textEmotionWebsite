from sqlalchemy.exc import InvalidRequestError, IntegrityError
from ..app import db
from ..model.user import User
from ..util.logger import get_logger as log

def FindOneOrCreate(ID=None, userName=None):
    query = User.query

    if ID is not None:
        query = query.filter_by(id=ID)
    if userName is not None:
        query = query.filter_by(UserName=userName)

    query = query.one_or_none()

    if query:
        query = query.__dict__
        
        query.pop("_sa_instance_state")

        return query
    else:
        if Create(userName) == 200:
            query = User.query.filter_by(UserName=userName).one_or_none()
            query = query.__dict__
            

            return query

def Create(userName):
    createUser = User(UserName=userName)

    try:
        db.session.add(createUser)
        db.session.commit()

        return 200
        

    except InvalidRequestError:
        log().error("Unable to create data")
        return 500

