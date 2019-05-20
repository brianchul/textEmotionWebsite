from app.model import Base, db

class Comment(Base):
    __tablename__ = "comment"
    
    FromArticle = db.Column(db.String(255), db.ForeignKey("Article.ArticleUrl", use_alter=True), nullable=False)
    Author = db.Column(db.String(255), db.ForeignKey("User.UserID", use_alter=True), nullable=False)
    CommentString = db.Column(db.TEXT)
    CommentTime = db.Column(db.DateTime())
    Language = db.Column(db.String(10), db.ForeignKey("Language.lang", use_alter=True), nullable=False)
    Keywords = db.relationship("keywords", order_by="keywords.id")