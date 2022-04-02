# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from flask_pymongo import PyMongo
from flask import session
from User import User
import secrets

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://admin:uEu9OcSgs1v42KG2@cluster0.3kizj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

#Initialize PyMongo
mongo = PyMongo(app)

# -- Session data --
app.secret_key = secrets.token_urlsafe(16)

# Fake users - DB
victor = User("victor@whereever.com", "a12341231", "victorandresvega")
josue = User("josue@whereever.com", "b5678567857", "josueestr")
kevin = User("kevin@whereever.com", "c0000000000", "kevilin")
all_users= {"victorandresvega": victor,"josueestr": josue,"kevilin": kevin}

# -- Routes section --
# LOGIN Route
@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        username = request.form['username']
        if username not in all_users:
            return 'Invalid username or password.'
        else:
            user = all_users[username] 
            password = request.form['password']
            password_correct = user.compare_password(password)
            if(password_correct):
                session['username'] = request.form['username']
                return redirect('/landing') 
            else:
               return 'Invalid username or password.' 
   

# LOGOUT Route
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/landing')

# LANDING Route
@app.route('/landing')
def landing():
    return render_template('landing.html')

# PROFILE Route
@app.route('/profile')
def profile():
    return render_template('Profile.html')