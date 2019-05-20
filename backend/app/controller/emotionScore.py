from sqlalchemy.exc import InvalidRequestError, IntegrityError
from ..app import db
from ..model.emotionScore import EmotionScore
from ..util.logger import get_logger as log

def Findone(commentID):
    query = EmotionScore.query.filter_by(CommentID=commentID).one_or_none()

    if query:
        query.__dict__.pop("_sa_instance_state")
        query = query.__dict__
        return query, 200
    else:
        return None, 404

def Create(commentID, score):
    r,c = Findone(commentID)
    if c == 200: return r,c
        
    newEmotionScore = EmotionScore(CommentID=commentID, Score=score)
    db.session.add(newEmotionScore)
    db.session.commit()
    return 200
    
