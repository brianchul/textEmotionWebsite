from sqlalchemy.exc import InvalidRequestError, IntegrityError
from ..app import db
from ..model.language import Language
from ..util.logger import get_logger as log

def FindOneOrCreate(lang):
    query = Language.query.filter_by(Lang=lang).one_or_none()

    if query:
        query = query.__dict__
        query.pop("_sa_instance_state")
        query.pop("id")
        query.pop("created_time")
        query.pop("updated_time")
        log().debug(query)
        return query, 200
    else:
        return None, 404

def Create(lang, isoName):
    createLang = Language(Lang=lang, Iso6391Name=isoName)

    try:
        db.session.add(createLang)
        db.session.commit()
        return 200

    except InvalidRequestError:
        log().error("Unable to create data")
        return 500



