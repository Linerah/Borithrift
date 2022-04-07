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
import certifi

from item import Item

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'boricuas'

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://admin:uEu9OcSgs1v42KG2@cluster0.3kizj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

#Initialize PyMongo
mongo = PyMongo(app, tlsCAFile=certifi.where())

# run this the first time, to create the collection
# mongo.db.create_collection('items')

# -- Session data --
app.secret_key = secrets.token_urlsafe(16)

# Fake users - DB
victor = User("victor@whereever.com", "a12341231", "victorandresvega")
josue = User("josue@whereever.com", "b5678567857", "josueestr")
kevin = User("kevin@whereever.com", "c0000000000", "kevilin")
all_users= {"victorandresvega": victor,"josueestr": josue,"kevilin": kevin}

# department set:
departments = {"women", "men"}

# filter list:
filters = {'new','tops', 'graphic tees', 'coats + jackets', 'bottoms', 'jeans', 'activewear', 'shoes','vintage', 'bottoms', 'sale'}

# top sellers this week:
top_sellers = {'victorvega', 'josueestrada', 'kevinlinera'}


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
@app.route('/landing', methods = ['GET', 'POST'])
def landing():
    if request.method == 'GET':
        items = Item.get_items(mongo)
    else:
        items = Item.get_filtered_items(mongo, request.form)
    return render_template('landing.html', departments=departments, filters=filters, top_sellers=top_sellers, items=items)

# PROFILE Route
@app.route('/profile')
def profile():
    return render_template('Profile.html')


@app.route('/seed_items')
def seed_items():
    # collection = mongo.db.items
    # document = {'test': 'test2'}
    # collection.insert_one(document)
    # Item.create_item('Yosemite Tee', 15.0, 'M', 'vintage', 'Men', 'its a tee', 'yosemite_tee.png', victor, mongo)
    # Item.create_item('Japan Tee', 25.0, 'L', 'graphic tees', 'Men', 'its a tee', 'japan_tee.png', josue, mongo)
    # Item.create_item('Running Jacket', 55.0, 'M', 'activewear', 'Men', 'its a tee', 'running_jacket_black.png', kevin, mongo)
    # Item.create_item('Spread Energy Tee', 20.0, 'S', 'graphic tees', 'Men', 'its a tee', 'spreed_energy_tee.png', victor, mongo)
    # Item.create_item('Gym Jacket', 45.0, 'S', 'activewear', 'Men', 'its a tee', 'running_jacket_green.png', kevin, mongo)
    return 'Seeded succesfuly'