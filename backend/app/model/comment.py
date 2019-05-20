from app.model import Base, db

class Comment(Base):
    __tablename__ = "comment"
    
    FromArticle = db.Column(db.Integer, db.ForeignKey("article.id", use_alter=True), nullable=False)
    Author = db.Column(db.Integer, db.ForeignKey("user.id", use_alter=True), nullable=False)
    CommentString = db.Column(db.TEXT)
    CommentTime = db.Column(db.DateTime())
    CommentPush = db.Column(db.String(5))
    Language = db.Column(db.String(10), db.ForeignKey("language.Lang", use_alter=True), nullable=False)
