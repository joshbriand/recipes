from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }


class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    cuisine = Column(String(250))
    meal = Column(String(250))
    date = Column(DateTime)
    picture = Column(String(500))
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'cuisine': self.cuisine,
            'process': self.process,
            'meal': self.meal,
            'ingredients': self.ingredients,
            'likes': self.likes,
            'date': self.date,
            'picture': self.image
       }


class Ingredient(Base):
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True)
    ingredient = Column(String(250))
    recipe_id = Column(Integer,ForeignKey('recipe.id'))
    recipe = relationship(Recipe)


class Process(Base):
    __tablename__ = 'process'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer,ForeignKey('recipe.id'))
    recipe = relationship(Recipe)
    process = Column(String(1000))


class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    comment = Column(String(250), nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)
    date = Column(DateTime)
    recipe_id = Column(Integer,ForeignKey('recipe.id'))
    recipe = relationship(Recipe)


class Like(Base):
    __tablename__ = 'like'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)
    recipe_id = Column(Integer,ForeignKey('recipe.id'))
    recipe = relationship(Recipe)

engine = create_engine('sqlite:///recipeindex.db')


Base.metadata.create_all(engine)
