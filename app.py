from flask_wtf import Form
from wtforms import validators
from wtforms import EmailField
###################################################################3
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import pandas as pd
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

################################################################################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
print("DATABASE URI:", app.config['SQLALCHEMY_DATABASE_URI'])
print("INSTANCE PATH:", app.instance_path)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    
    
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/help')
def help():
    return render_template("help.html")


@app.route('/terms')
def terms():
    return render_template("tc.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return render_template("login.html", form=form)
    return render_template("login.html", form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")
    return render_template('signup.html', form=form)


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


@app.route("/disindex")

def disindex():
    return render_template("disindex.html")




@app.route("/heart")
@login_required
def heart():
    return render_template("heart.html")




@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

############################################################################################################

@app.route('/predictheart', methods=['POST'])
def predictheart():
    
    #input_features = [float(x) for x in request.form.values()]
    
    age1 = int(request.form.get("age"))
    sex = int(request.form.get("Gender"))
    chestPain = int(request.form.get("ChestPain") )
    resbp =  int(request.form.get("resting bp"))
    chole =  int(request.form.get("cholesterol"))
    fastbs = int(request.form.get("Fasting Blood Sugar"))
    restecg = int( request.form.get("Resting ECG"))
    maxheart =  int(request.form.get("Maximus Heart Rate"))
    exerciseangia = int(request.form.get("Exercise Angina") )
    oldpeak = float( request.form.get("Old Peak"))
    stslope = float(request.form.get("ST slope"))

    input_data = (age1,sex,chestPain,resbp,chole,fastbs,restecg,maxheart,exerciseangia,oldpeak,stslope)

    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)    
    
    model_path = os.path.join(basedir, 'RFmodel88_test02.sav')
    loaded_RFmodel = pickle.load(open(model_path, 'rb'))
    
    prediction = loaded_RFmodel.predict(input_data_reshaped)

    if prediction[0] == 1:
        res_val = "A high risk of Heart Disease"
    else:
        res_val = "A low risk of Heart Disease"
    return render_template('heart_result.html', prediction_text='Patient has {}'.format(res_val))

############################################################################################################

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
