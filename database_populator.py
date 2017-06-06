from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from database_setup import Base, User, Recipe, Comment, Like, Process, Ingredient

engine = create_engine('sqlite:///recipeindex.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create a user
User1 = User(name="Josh Briand", email="joshbriand@gmail.com")
session.add(User1)
session.commit()

print "added menu items!"
'''
newRecipe = Recipe(name="Test Recipe", cuisine="German", meal="Dinner", date=datetime.now(), picture="http://via.placeholder.com/200x200", user_id=1)
session.add(newRecipe)
session.commit()
'''
recipeID = session.query(Recipe).filter_by(name="Test Recipe").one().id
newIngredient = Ingredient(ingredient="first", recipe_id=recipeID)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="second", recipe_id=recipeID)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="third", recipe_id=recipeID)
session.add(newIngredient)
session.commit()
newProcess = Process(process="first step", recipe_id=recipeID)
session.add(newProcess)
session.commit()
newProcess = Process(process="second step", recipe_id=recipeID)
session.add(newProcess)
session.commit()
newProcess = Process(process="third step", recipe_id=recipeID)
session.add(newProcess)
session.commit()
