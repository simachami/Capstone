from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class AllRecipes():
    all_recipes_ids = ['654959', '511728', '654883', '654928', '654944', '654913', '634698', '75081', '715567', '634618', '634559', '634629', '637876', '638420', '638308', '638174', '638125', '638257', '662271', '636736', '648247', '653008', '1697787', '652330', '664658', '664689', '664663', '664699', '664650', '664697', '664472', '1095748', '1096306', '664396', '664419', '1095996']

class PastaRecipes():
    pasta_recipe_ids_list = ['654959', '511728', '654883', '654928', '654944', '654913']

class BeefRecipes():
    beef_recipe_ids_list = ['634698', '75081', '715567', '634618', '634559', '634629']

class ChickenRecipes():
    chicken_recipe_ids_list = ['637876', '638420', '638308', '638174', '638125', '638257']

class SeafoodRecipes():
    seafood_recipe_ids_list = ['662271', '636736', '648247', '653008', '1697787', '652330']

class VeggieRecipes():
    veggie_recipe_ids_list = ['664658', '664689', '664663', '664699', '664650', '664697']

class VeganRecipes():
    vegan_recipe_ids_list = ['664472', '1095748', '1096306', '664396', '664419', '1095996']

class RecipeForm(FlaskForm):
    title = 'Temp Title'
    summary = 'temp summary'
    input_text = StringField('Input:', validators=[ DataRequired()])
    submit = SubmitField('Get Recipe')

class LoginForm(FlaskForm):
    email = StringField('Email:', validators=[ DataRequired()])
    password = PasswordField('Password:', validators=[ DataRequired()])
    submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
    first_name = StringField('First Name: ')
    last_name = StringField('Last Name: ')
    username = StringField('Username:',validators=[ DataRequired() ])
    email = StringField('Email:', validators=[ DataRequired() ])
    password = PasswordField('Password:', validators=[ DataRequired() ])
    verify_password = PasswordField('Confirm Password:', validators=[ DataRequired(), EqualTo('password') ])
    submit = SubmitField('Sign Up')



    