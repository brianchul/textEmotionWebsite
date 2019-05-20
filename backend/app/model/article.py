from app.model import Base, db

class Article(Base):
    __tablename__ = "article"

    ArticleUrl = db.Column(db.String(255), unique=True, primary_key=True)
    ArticleTitle = db.Column(db.String(255))
    ArticleAuthor = db.Column(db.Integer, db.ForeignKey("user.id", use_alter=True), nullable=False)
    Content = db.Column(db.TEXT)
    Language = db.Column(db.String(10), db.ForeignKey("language.Lang", use_alter=True), nullable=False)