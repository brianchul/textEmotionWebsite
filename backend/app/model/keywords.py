from app.model import Base, db

class Keywords(Base):
    # which kind of endorsement
    __tablename__ = "keywords"

    CommentID = db.Column(db.Integer, db.ForeignKey("comment.id", use_alter=True), nullable=False)
    Phase = db.Column(db.TEXT)