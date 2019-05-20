from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import DefaultMeta

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Default_base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_time = db.Column(db.DateTime(), default=db.func.now())
    updated_time = db.Column(
        db.DateTime(), default=db.func.now(), onupdate=db.func.now()
        )

Base = declarative_base(cls=Default_base, name='Default',
                        metaclass=DefaultMeta)
