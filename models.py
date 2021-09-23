from sqlalchemy import exc
import errors
from app import db


class BaseModelMixin:

    @classmethod
    def by_id(cls, obj_id):
        obj = cls.query.get(obj_id)
        if obj:
            return obj
        else:
            raise errors.NotFound

    def add(self):
        db.session.add(self)
        try:
            db.session.commit()
        except exc.IntegrityError:
            raise errors.BadLuck

    def delete(self):
        db.session.delete(self)
        try:
            db.session.commit()
        except exc.IntegrityError:
            raise errors.NotFound


class Advertisement(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    descriptions = db.Column(db.String(120))
    create_date = db.Column(db.Date)
    owner = db.Column(db.Integer, unique=True)

    def __str__(self):
        return '<Advertisement {}>'.format(self.title)

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'descriptions': self.descriptions,
            'create_date': self.create_date,
            'owner': self.owner
        }


db.create_all()
