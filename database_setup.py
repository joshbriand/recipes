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


class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    cuisine = Column(String(250))
    meal = Column(String(250))
    date = Column(DateTime)
    picture = Column(String(500))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'cuisine': self.cuisine,
            'meal': self.meal,
            'date': self.date,
            'picture': self.picture
        }


class Ingredient(Base):
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True)
    ingredient = Column(String(250))
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    recipe = relationship(Recipe)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'ingredient': self.ingredient
        }


class Process(Base):
    __tablename__ = 'process'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    recipe = relationship(Recipe)
    process = Column(String(1000))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'process': self.process
        }


class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    comment = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    date = Column(DateTime)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    recipe = relationship(Recipe)


class Like(Base):
    __tablename__ = 'like'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    recipe = relationship(Recipe)


engine = create_engine('sqlite:///recipeindex.db')


Base.metadata.create_all(engine)
