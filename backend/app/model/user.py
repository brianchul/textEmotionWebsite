from app.model import Base, db


class User(Base):
    __tablename__ = "user"

    UserName = db.Column(db.String(255), primary_key=True, unique=True)
