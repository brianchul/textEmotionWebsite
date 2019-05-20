from app.model import Base, db

class Article(Base):
    __tablename__ = "Article"

    ArticleUrl = db.Column(db.String(255), unique=True, primary_key=True,)
    ArticleAuthor = db.Column(db.String(255), db.ForeignKey("User.UserID", use_alter=True), nullable=False)
    Content = db.Column(db.TEXT)
    Language = db.Column(db.String(10), db.ForeignKey("Language.lang", use_alter=True), nullable=False)
    