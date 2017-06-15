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

newUser = User(name="Josh Briand", email="joshbriand@gmail.com")
session.add(newUser)
session.commit()
newUser = User(name="Sean Casey", email="seancasey@gmail.com")
session.add(newUser)
session.commit()
print "Added users"
newRecipe = Recipe(
    name="Panko Fish",
    cuisine="Japanese",
    meal="Dinner",
    date=datetime.now(),
    picture="https://www.takemefishing.org/tmf/assets/images/fish/albacore-464x170.png",
    user_id=2)
session.add(newRecipe)
session.commit()
recipe_id = session.query(Recipe).filter_by(user_id=2).first().id
newIngredient = Ingredient(
    ingredient="3/4 cup Japanese panko breadcrumbs",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(
    ingredient="3/4 cup Parmesan cheese finely grated",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(
    ingredient="3 tablespoons unsalted butter room temperature",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(
    ingredient="3 tablespoons mayonnaise",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(
    ingredient="3 green onions, green tops only thinly sliced",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(
    ingredient="1 teaspoon Worchestershire sauce",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(
    ingredient="1/2 teaspoon Tabasco or other hot pepper sauce",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(
    ingredient="1 1/2 tablespoons lemon juice freshly squeezed (approx. 1/2 lemon)",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(
    ingredient="salt and pepper to taste",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(
    ingredient="4 white fish fillets approx. 6 oz; 1/2 to 3/4 inch thick",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(
    ingredient="2 tablespoons fresh flat-leaf parsely finely chopped",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newProcess = Process(
    process="Preheat oven to 400f. Lightly butter a baking dish or individual grain dishes for the fillets.",
    recipe_id=recipe_id)
session.add(newProcess)
session.commit()
newProcess = Process(
    process="n medium bowl, mix together the cheese, breadcrumbs, butter, mayonnaise, green onions, Worcestershire sauce, Tabasco and lemon juice; season to taste with salt and pepper. Set aside until needed.",
    recipe_id=recipe_id)
session.add(newProcess)
session.commit()
newProcess = Process(
    process="Pat the fish fillets completely dry with paper towels (removing the moisture ensures they won't get mushy while baking); season generously with salt and pepper. Arrange the fish in a lightly buttered baking dish or individual gratin dishes.",
    recipe_id=recipe_id)
session.add(newProcess)
session.commit()
newProcess = Process(
    process="Spread about 3 tablespoons of the cheese mixture over each fillet.",
    recipe_id=recipe_id)
session.add(newProcess)
session.commit()
newProcess = Process(
    process="Place in preheated oven and bake until bubbly and almost cooked through, about 10 minutes. Temperature should be approximately 125-130f when tested at thickest part of fillet with meat thermometer.",
    recipe_id=recipe_id)
session.add(newProcess)
session.commit()
newProcess = Process(
    process="Move fillets to broiler for 2 to 3 minutes to brown and crisp the tops. When done, the fish should flake easily with a fork.",
    recipe_id=recipe_id)
session.add(newProcess)
session.commit()
newProcess = Process(
    process="Remove from oven, garnish with fresh parsley and serve immediately.",
    recipe_id=recipe_id)
session.add(newProcess)
session.commit()
newRecipe = Recipe(
    name="Roast Beetroot and Sweet Potato Buddha Bowl with Spicy Tahini Honey Dressing",
    cuisine="Vegan",
    meal="Dinner",
    date=datetime.now(),
    picture="http://www.thefoodiecorner.gr/wp-content/uploads/2017/03/Roast-Beetroot-and-Sweet-Potato-Buddha-Bowl-with-Spicy-Tahini-Honey-Dressing-www.thefoodiecorner.gr-8-1.jpg",
    user_id=1)
session.add(newRecipe)
session.commit()
recipe_id = session.query(Recipe).filter_by(user_id=1).first().id
newIngredient = Ingredient(
    ingredient="500g sweet potato cubed",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(
    ingredient="400g beetroot, cubed",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="4 tbs olive oil", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="1 tsp salt", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="1 cup brown rice", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(
    ingredient="6-8 handfuls greens",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(
    ingredient="3-4 tbs dried cranberries",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(
    ingredient="2-3 tbs sunflower seeds",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="For the dressing:", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="4 tbs tahini", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="2 tbs honey", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="2 tbs olive oil", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="2 tbs water", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(
    ingredient="1 tbs orange juice",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="1/4 tsp cinnamon", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="1/4 tsp salt", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(
    ingredient="1/8 tsp chilli powder",
    recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newIngredient = Ingredient(ingredient="1/8 tsp cumin", recipe_id=recipe_id)
session.add(newIngredient)
session.commit()
newProcess = Process(process='''Preheat oven to 180C fan assisted (200C
conventional). Line two baking sheets with grease proof paper. Put the sweet
potato, 2 tablespoons of oil and half a teaspoon of salt in a bowl and mix with
your hands to coat. Spread it out on a baking sheet (the pieces need to have
room, no crowding!). Do the same with the beetroot, the other 2 tbs oil and half
 teaspoon salt. Put both sheets in the oven to roast the veggies. The beetroot
 should need about 25 minutes till softened and the sweet potato about 30 till
 softened and starting to brown.''', recipe_id=recipe_id)
session.add(newProcess)
session.commit()
newProcess = Process(
    process="Boil the rice according to instructions.",
    recipe_id=recipe_id)
session.add(newProcess)
session.commit()
newProcess = Process(
    process="To make the dressing whisk all the ingredients in a bowl. If needed warm it up a bit in the microwave to make it runnier.",
    recipe_id=recipe_id)
session.add(newProcess)
session.commit()
newProcess = Process(process='''Assemble the bowls with a little of each
vegetable, some rice, a small handful of spinach and rocket, a sprinkling of
cranberries and sunflower seeds, and a drizzle of dressing. Start modestly with
the dressing as it's strong tasting, and add more if desired. Serve warm or at
room temperature.''', recipe_id=recipe_id)
session.add(newProcess)
session.commit()
print "recipes added"
like = Like(recipe_id=1, user_id=2)
session.add(like)
session.commit()
like = Like(recipe_id=1, user_id=1)
session.add(like)
session.commit()
like = Like(recipe_id=2, user_id=2)
session.add(like)
session.commit()
print "likes added"
newComment = Comments(
    recipe_id=1,
    user_id=1,
    date=datetime.now(),
    comment="Great recipe, Sean!")
session.add(newComment)
session.commit()
print "comment added"
