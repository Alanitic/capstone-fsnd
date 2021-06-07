from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import backref, relationship
import os

# database_name = "capstone"
# database_path = "postgresql://{}/{}".format('localhost:5432', database_name)

database_path = os.environ['DB_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, db_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Movie(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    releaseDate = Column(DateTime)

    def __init__(self, title, release_date):
        self.title = title
        self.releaseDate = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'releaseDate': self.releaseDate
        }


class Actor(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

    def __init__(self, name, age, gender):
        self.name = name,
        self.age = age,
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }


class Role(db.Model):
    actor_id = Column(Integer, ForeignKey(Actor.id), primary_key=True)
    movie_id = Column(Integer, ForeignKey(Movie.id), primary_key=True)
    role = Column(String)

    actor = relationship(Actor, backref=backref('Roles', cascade='all, delete'))
    movie = relationship(Movie, backref=backref('Roles', cascade='all, delete'))
