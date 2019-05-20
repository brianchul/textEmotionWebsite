from sqlalchemy.exc import InvalidRequestError, IntegrityError
from ..app import db
from ..model.user import User
from ..util.logger import get_logger as log

def FindOneOrCreate(userID):
    query = User.query.filter_by(UserID=userID).one_or_none()

    if query:
        query = query.__dict__
        query.pop("_sa_instance_state")
        query.pop("id")
        query.pop("created_time")
        query.pop("updated_time")
        log().debug(query)
        return query
    else:
        createUser = User(UserID=userID)
        try:
            db.session.add(createUser)
            db.session.commit()
            FindOneOrCreate(userID)

        except InvalidRequestError:
            log().error("Unable to create data")
            return 500



