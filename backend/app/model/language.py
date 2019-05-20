from app.model import Base, db


class Language(Base):
    __tablename__ = "Language"

    Lang = db.Column(db.String(10), primary_key=True, unique=True)
    Iso6391Name = db.Column(db.String(20))
