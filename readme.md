#Josh Briand's Recipe Catalog v 1.0 06/15/2017

##Introduction
The purpose of this web app is to provide a list of recipes within a variety of
meal and cuisine types.  The web app also provides a user registration and
authentication system.  Registered users can add recipes, edit and delete their
own recipes, add comments, edit and delete their own comments, like recipes and
unlike recipes they have liked already.  The web app uses 6 database tables to
manage users, recipes, ingredients, processes, comments and likes.

##Installation
To run the web app locally you must have Vagrant and Python 2.7 installed
on your computer.  Installation instructions for Vagrant can be found here:
https://www.vagrantup.com/docs/installation/
You can download Python here:
https://www.python.org/downloads/
When both are installed...
1. Copy and paste the project directory into your Vagrant folder
2. Open Terminal, navigate to your Vagrant folder and run 'vagrant up'
3. Run 'vagrant ssh'
4. Navigate to your Vagrant folder then to the project folder
5. Run 'python database_populator.py' to populate the database
6. Run 'python project.py'
7. Using your browser go to http://localhost:8000

##Usage
The web app contains 15 handlers.
1. **gconnect**: Allows user to log in using Google-Plus Oauth.
2. **disconnect**: Disconnects user from site.
3. **showRecipes**: Shows all recipes in the database.  Allows user to filter by
cuisine type, meal type or user.  Allows user to order by newest first, oldest
first, most popular or alphabetically.
4. **addRecipe**: Allows user to add a new recipe to the database.
5. **showRecipe**: Show recipe details (ingredients and method), comments and
likes.  Provides a link to leave a new comment.  Allows user to like or unlike
(if liked already) recipe.
7. **editRecipe**: Allows user to edit a recipe that they created.
8. **deleteRecipe**: Allows user to delete a recipe that they created.
9. **likeRecipe**: Functionality for user to like a recipe.
10. **unlikeRecipe**: Functionality for user to unlike (if already liked) a
recipe.
11. **addComment**: Allows user to leave a comment for a recipe.
12. **editComment**: Allows user to edit a comment they created.
13. **deleteComment**: Allows user to delete a comment they created.
14. **recipesJSON**: JSON endpoint that serves information about all recipes (
cuisine type, meal type, data created, id, name and picture url).
15. **recipeJSON**: JSON endpoint that serves information about a specific
recipe (ingredients, process, cuisine type, meal type, data created, id, name
and picture url)

##Contact Info
E-mail: joshbriand@gmail.com
