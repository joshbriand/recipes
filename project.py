from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Recipe, Comment, Like, Process, Ingredient
from flask import session as login_session
import random
import string
import datetime
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import simplejson
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('google_client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Recipe Application"

# Connect to Database and create database session
engine = create_engine('sqlite:///recipeindex.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create anti-forgery state token
def generateState():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return state


@app.route('/gconnect', methods=['POST'])
def gconnect():
    state = generateState()
    # Validate state token

    '''
    if request.args.get('state') != login_session['state']:
        response = make_response(simplejson.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/simplejson'
        print "error 1"
        return response
    '''
    # Obtain authorization code
    code = request.data
    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('google_client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
        print "success 3 %s" % credentials
    except FlowExchangeError:
        response = make_response(
            simplejson.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['email'] = data['email']
    login_session['provider'] = 'google'

    user_id = getUserID(login_session['email'])
    if user_id is None:
        createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    return output

    # DISCONNECT - Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session['access_token']
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    if access_token is None:
 	print 'Access Token is None'
    	response = make_response(simplejson.dumps('Current user not connected.'), 401)
    	response.headers['Content-Type'] = 'application/simplejson'
    	return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
	del login_session['access_token']
    	del login_session['gplus_id']
    	del login_session['username']
    	del login_session['email']
    	response = make_response(simplejson.dumps('Successfully disconnected.'), 200)
    	response.headers['Content-Type'] = 'application/simplejson'
    	return response
    else:
    	response = make_response(simplejson.dumps('Failed to revoke token for given user.', 400))
    	response.headers['Content-Type'] = 'application/simplejson'
    	return response



@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            del login_session['gplus_id']
            del login_session['access_token']
        del login_session['username']
        del login_session['email']
        del login_session['user_id']
        flash ("You have been logged out")
        print "User logged out"
        return redirect(url_for('showRecipes'))
    else:
        flash("You were not logged in to begin with!")
        return redirect(url_for('showRecipes'))

#Show all recipes
@app.route('/')
@app.route('/recipes/', methods=['GET', 'POST'])
def showRecipes():
    if request.method == 'POST':
        pass
    else:
        recipes = session.query(Recipe).order_by(Recipe.date)
        users = session.query(User).order_by(User.id)
        return render_template('recipes.html', recipes=recipes, users=users)


#Create a recipe
@app.route('/addrecipe/', methods=['GET', 'POST'])
def addRecipe():
    if request.method == 'POST':
        error = ""
        if request.form['cuisine'] == "Choose One":
            error = "You must choose a cuisine type!"
        elif request.form['meal'] == "Choose One":
            error = "You must choose a meal type!"
        #flash
        #error and rerender
        cuisine = request.form['cuisine']
        meal = request.form['meal']
        name = request.form['name']
        ingredients = request.form['ingredients']
        ingredientList = ingredients.split("\n")
        process = request.form['process']
        processList = process.split("\n")
        picture = request.form['picture']
        user_id = login_session['user_id']
        date = datetime.datetime.now()
        if error != "":
            flash(error)
            return render_template('addrecipe.html', name=name, ingredients=ingredients, process=process, picture=picture, cuisine=cuisine, meal=meal)
        newRecipe = Recipe(name=name, cuisine=cuisine, meal=meal, date=date, picture=picture, user_id=user_id)
        session.add(newRecipe)
        session.commit()
        recipe_id = session.query(Recipe).filter_by(name=name).one().id
        for ingredient in ingredientList:
            newIngredient = Ingredient(ingredient=ingredient, recipe_id=recipe_id)
            session.add(newIngredient)
            session.commit()
        for process in processList:
            newProcess = Process(process=process, recipe_id=recipe_id)
            session.add(newProcess)
            session.commit()
        flash('New Recipe %s Successfully Created' % newRecipe.name)
        return redirect(url_for('showRecipe', recipe_id=recipe_id))
        #return to recipe (no s!)
    else:
        if 'username' not in login_session:
            return redirect('/')
        else:
            cuisine = "Choose One"
            meal = "Choose One"
            date = datetime.datetime.now()
            print date
            return render_template('addrecipe.html', meal=meal, cuisine=cuisine)


#Show a recipe
@app.route('/recipe/<int:recipe_id>/')
def showRecipe(recipe_id):
    if recipeExists(recipe_id):
        print "ok"
        recipe = session.query(Recipe).filter_by(id=recipe_id).one()
        ingredients = session.query(Ingredient).filter_by(recipe_id=recipe_id).all()
        processes = session.query(Process).filter_by(recipe_id=recipe_id).all()
        return render_template('recipe.html', recipe=recipe, ingredients=ingredients, processes=processes)
    print "not ok"
    flash('Recipe does not exist')
    return redirect('/')



#Edit a recipe
@app.route('/editrecipe/')
def editRecipe():
    return render_template('editrecipe.html')

#Delete a recipe
@app.route('/deleterecipe/<int:recipe_id>/', methods=['GET', 'POST'])
def deleteRecipe(recipe_id):
    if recipeExists(recipe_id):
        author = session.query(Recipe).filter_by(id=recipe_id).one().user
        recipeToDelete = session.query(Recipe).filter_by(id=recipe_id).one()
        if 'username' in login_session:
            if author.id == login_session['user_id']:
                if request.method == "POST":
                    print "here"
                    if request.form['delete'] == "Yes":
                        session.delete(recipeToDelete)
                        session.commit()
                        flash('Recipe Successfully Deleted')
                        return redirect('/')
                    else:
                        return redirect('/recipe/', recipe_id=recipe_id)
                else:
                    return render_template('deleterecipe.html', recipe=recipeToDelete)
            else:
                flash('You are not authorized to delete this recipe')
        else:
            flash('User not logged in')
    else:
        flash('Recipe does not exist')
    return redirect('/')


#Add a comment
@app.route('/addcomment/')
def addComment():
    return render_template('addcomment.html')


def recipeExists(recipe_id):
    q = session.query(Recipe).filter_by(id=recipe_id)
    return session.query(q.exists()).scalar()


def createUser(login_session):
    newUser = User(name = login_session['username'], email =
        login_session['email'])
    session.add(newUser)
    session.commit()
    print "user created"
    user = session.query(User).filter_by(email = login_session['email']).one()
    users = session.query(User).all()
    for user in users:
        print user.username
    return user.id

def getUserInfo(user_id):
    user = session.query(User).filter_by(id = user_id).one()
    return user

def getUserID(email):
    try:
        user = session.query(User).filter_by(email = email).one()
        return user.id
    except:
        return None

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
