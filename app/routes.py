from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from app import app
from requests import get
import requests
from app.forms import LoginForm, SignUpForm, AllRecipes, PastaRecipes, BeefRecipes, ChickenRecipes, SeafoodRecipes, VeggieRecipes, VeganRecipes, DessertRecipes
from app.models import User


@app.route('/')
def home():
    return render_template('index.jinja', recipe=None)

@app.route('/search', methods=['GET', 'POST'])
def get_recipe_details():
    if request.method == 'POST':
        recipe_id = request.form.get('recipe_id')
    else:
        recipe_id = request.args.get('recipe_id')

    if recipe_id:
        #print(app.config.get('SECRET KEY'))
        url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={app.config.get('API_KEY')}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            recipe_data = {
                'title': data.get('title', ''),
                'summary': data.get('summary', ''),
                'image_url': data.get('image', '')
            }
            return render_template('index.jinja', recipe=recipe_data)
    
    return render_template('index.jinja', recipe=None)



#All recipes api call
@app.route('/recipes')
def get_all_recipes():
    all_recipe_json_list = []
    recipe_list = AllRecipes()
    for recipe_id in recipe_list.all_recipes_ids_list:
        url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={app.config.get('API_KEY')}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            recipe_data = {
                'title': data.get('title', ''),
                'summary': data.get('summary', ''),
                'readyInMinutes': data.get('readyInMinutes', ''),
                'servings': data.get('servings', ''),
                'image_url': data.get('image', ''),
                'source_url': data.get('sourceUrl', '')
            }
            all_recipe_json_list.append(recipe_data)
    return render_template('pasta.jinja', recipes=all_recipe_json_list)
    
    


#Pasta API Calls
@app.route('/recipes/pasta')
def get_pasta_recipes():
    pasta_recipe_json_list = []
    recipe_list = PastaRecipes()
    for recipe_id in recipe_list.pasta_recipe_ids_list:
        url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={app.config.get('API_KEY')}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            recipe_data = {
                'title': data.get('title', ''),
                'summary': data.get('summary', ''),
                'readyInMinutes': data.get('readyInMinutes', ''),
                'servings': data.get('servings', ''),
                'image_url': data.get('image', ''),
                'source_url': data.get('sourceUrl', '')
            }
            pasta_recipe_json_list.append(recipe_data)
    return render_template('pasta.jinja', recipes=pasta_recipe_json_list)



#Beef API Calls
@app.route('/recipes/beef')
def get_beef_recipes():
    beef_recipe_json_list = []
    recipe_list = BeefRecipes()
    for recipe_id in recipe_list.beef_recipe_ids_list:
        url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={app.config.get('API_KEY')}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            recipe_data = {
                'title': data.get('title', ''),
                'summary': data.get('summary', ''),
                'image_url': data.get('image', '')
            }
            beef_recipe_json_list.append(recipe_data)
    return render_template('beef.jinja', recipes=beef_recipe_json_list)



#Chicken API Calls
@app.route('/recipes/chicken')
def get_chicken_recipes():
    chicken_recipe_json_list = []
    recipe_list = ChickenRecipes()
    for recipe_id in recipe_list.chicken_recipe_ids_list:
        url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={app.config.get('API_KEY')}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            recipe_data = {
                'title': data.get('title', ''),
                'summary': data.get('summary', ''),
                'image_url': data.get('image', '')
            }
            chicken_recipe_json_list.append(recipe_data)
    return render_template('chicken.jinja', recipes=chicken_recipe_json_list)


#Seafood API Calls
@app.route('/recipes/seafood')
def get_seafood_recipes():
    seafood_recipe_json_list = []
    recipe_list = SeafoodRecipes()
    for recipe_id in recipe_list.seafood_recipe_ids_list:
        url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={app.config.get('API_KEY')}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            recipe_data = {
                'title': data.get('title', ''),
                'summary': data.get('summary', ''),
                'image_url': data.get('image', '')
            }
            seafood_recipe_json_list.append(recipe_data)
    return render_template('seafood.jinja', recipes=seafood_recipe_json_list)


#vegetarian API Calls
@app.route('/recipes/vegetarian')
def get_veggie_recipes():
    veggie_recipe_json_list = []
    recipe_list = VeggieRecipes()
    for recipe_id in recipe_list.veggie_recipe_ids_list:
        url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={app.config.get('API_KEY')}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            recipe_data = {
                'title': data.get('title', ''),
                'readyInMinutes': data.get('readyInMinutes', ''),
                'summary': data.get('summary', ''),
                'image_url': data.get('image', '')
            }
            veggie_recipe_json_list.append(recipe_data)
    return render_template('veggie.jinja', recipes=veggie_recipe_json_list)

#vegetarian API Calls
@app.route('/recipes/vegan')
def get_vegan_recipes():
    vegan_recipe_json_list = []
    recipe_list = VeganRecipes()
    for recipe_id in recipe_list.vegan_recipe_ids_list:
        url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={app.config.get('API_KEY')}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            recipe_data = {
                'title': data.get('title', ''),
                'summary': data.get('summary', ''),
                'image_url': data.get('image', '')
            }
            vegan_recipe_json_list.append(recipe_data)
    return render_template('vegan.jinja', recipes=vegan_recipe_json_list)

#Dessert API Calls
@app.route('/recipes/dessert')
def get_dessert_recipes():
    dessert_recipe_json_list = []
    recipe_list = DessertRecipes()
    for recipe_id in recipe_list.dessert_recipe_ids_list:
        url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={app.config.get('API_KEY')}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            recipe_data = {
                'title': data.get('title', ''),
                'summary': data.get('summary', ''),
                'readyInMinutes': data.get('readyInMinutes', ''),
                'servings': data.get('servings', ''),
                'image_url': data.get('image', ''),
                'source_url': data.get('sourceUrl', '')
            }
            dessert_recipe_json_list.append(recipe_data)
    return render_template('dessert.jinja', recipes=dessert_recipe_json_list)

def check_active_user():
    if current_user.is_authenticated:
        return redirect(url_for(home))

@app.route('/signin', methods=['Get', 'POST'])
def sign_in():
    signin_form = LoginForm()
    if signin_form.validate_on_submit():
        email = signin_form.email.data
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(signin_form.password.data):
            login_user(user)
            print(current_user.username)
            flash(f'{signin_form.email.data} successfully logged in!' ,category='success')
            return redirect('/')
        else:
            flash(f'Invalid User Info, Please try again!', category='alert')
    return render_template('signin.jinja', form=signin_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('sign_in'))

@app.route('/signup', methods=['Get', 'POST'])
def sign_up():
    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        user_info = {
            'first_name' : signup_form.first_name.data,
            'last_name' : signup_form.last_name.data,
            'username' : signup_form.username.data,
            'email' : signup_form.email.data,
        }
        try:
            user = User()
            user.from_dict(user_info)
            user.hash_password(signup_form.password.data)
            user.commit()
            flash(f'{user.first_name if user.first_name else user.username} registered', category='success')
            login_user(user)
            return redirect(url_for('home'))
        except:
            flash(f'Username or Email is already taken. Please try again!', category='alert')
    return render_template('signup.jinja', form=signup_form)







