from app.model import Base, db

class EmotionScore(Base):
    __tablename__ = "emotionScore"

    CommentID = db.Column(db.Integer, db.ForeignKey("comment.id", use_alter=True), nullable=False)
    Score = db.Column(db.Float())
