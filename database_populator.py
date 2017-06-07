from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from database_setup import Base, User, Recipe, Comments, Like, Process, Ingredient

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

'''
like = Like(recipe_id=1, user_id=2)
session.add(like)
session.commit()
like = Like(recipe_id=2, user_id=2)
session.add(like)
session.commit()


User1 = User(name="Josh Briand", email="joshbriand@gmail.com")
session.add(User1)
session.commit()
User1 = User(name="Sean Casey", email="seancasey@gmail.com")
session.add(User1)
session.commit()
print "added menu items!"
newRecipe = Recipe(name="Panko Fish", cuisine="Japanese", meal="Dinner", date=datetime.now(), picture="http://via.placeholder.com/200x200", user_id=2)
session.add(newRecipe)
session.commit()
recipe_id = session.query(Recipe).filter_by(user_id=2).first().id
print recipe_id
newIngredient = Ingredient(ingredient="3/4 cup Japanese panko breadcrumbs", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="3/4 cup Parmesan cheese finely grated", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="3 tablespoons unsalted butter room temperature", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="3 tablespoons mayonnaise", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="3 green onions, green tops only thinly sliced", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="1 teaspoon Worchestershire sauce", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="1/2 teaspoon Tabasco or other hot pepper sauce", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="1 1/2 tablespoons lemon juice freshly squeezed (approx. 1/2 lemon)", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="salt and pepper to taste", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="4 white fish fillets approx. 6 oz; 1/2 to 3/4 inch thick", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="2 tablespoons fresh flat-leaf parsely finely chopped", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()

newProcess = Process(process="Preheat oven to 400f. Lightly butter a baking dish or individual grain dishes for the fillets.", recipe_id=recipe_id)
session.add(newProcess)
session.commit()
newProcess = Process(process="n medium bowl, mix together the cheese, breadcrumbs, butter, mayonnaise, green onions, Worcestershire sauce, Tabasco and lemon juice; season to taste with salt and pepper. Set aside until needed.", recipe_id=recipe_id)
session.add(newProcess)
session.commit()
newProcess = Process(process="Pat the fish fillets completely dry with paper towels (removing the moisture ensures they won't get mushy while baking); season generously with salt and pepper. Arrange the fish in a lightly buttered baking dish or individual gratin dishes.", recipe_id=recipe_id)
session.add(newProcess)
session.commit()
newProcess = Process(process="Spread about 3 tablespoons of the cheese mixture over each fillet.", recipe_id=recipe_id)
session.add(newProcess)
session.commit()
newProcess = Process(process="Place in preheated oven and bake until bubbly and almost cooked through, about 10 minutes. Temperature should be approximately 125-130f when tested at thickest part of fillet with meat thermometer.", recipe_id=recipe_id)
session.add(newProcess)
session.commit()
newProcess = Process(process="Move fillets to broiler for 2 to 3 minutes to brown and crisp the tops. When done, the fish should flake easily with a fork.", recipe_id=recipe_id)
session.add(newProcess)
session.commit()
newProcess = Process(process="Remove from oven, garnish with fresh parsley and serve immediately.", recipe_id=recipe_id)
session.add(newProcess)
session.commit()
'''
print "added!"
