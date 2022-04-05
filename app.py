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
from typing import Collection
from flask import Flask
from flask import render_template
from flask import request, redirect
from flask_pymongo import PyMongo
from flask import session
from User import User
import secrets
import certifi

from item import Item
from Profile import Profile
# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'cluster0'

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://SDS:Boricuas@cluster0.zc52h.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority"

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
@app.route('/profile',methods = ['GET', 'POST'])
def profile():

    username=session.get('username')
    collection=mongo.db.items
    profile=Profile.get_profile(username,mongo)
    if request.method == 'GET':
        user_items=list(collection.find({"username":username}))
    else: 
        user_items=list(collection.find({"username":username}))
    return render_template('Profile.html',session=session,user_items=user_items,profile=profile)


@app.route('/seed_items')
def seed_items():
    # collection = mongo.db.items
    # victorItem1=Item.create_item('Yosemite Teefewewfew', 15.0, 'M', 'vintage', 'Men', 'its a tee', 'yosemite_tee.png', victor, mongo)
    # josueItem1=Item.create_item('Japan Teefewewf', 25.0, 'L', 'graphic tees', 'Men', 'its a tee', 'japan_tee.png', josue, mongo)
    # kevinItem1=Item.create_item('Running Jackefewweft', 55.0, 'M', 'activewear', 'Men', 'its a tee', 'running_jacket_black.png', kevin, mongo)
    # victorItem2=Item.create_item('Spread Energy Teefwefwe', 20.0, 'S', 'graphic tees', 'Men', 'its a tee', 'spreed_energy_tee.png', victor, mongo)
    # kevinItem2=Item.create_item('Gym Jacketfdsf', 45.0, 'S', 'activewear', 'Men', 'its a tee', 'running_jacket_green.png', kevin, mongo)
    collection = mongo.db.profiles
    victorP=Profile.create_profile("victorandresvega", 5.0,10,"https://images.unsplash.com/photo-1529665253569-6d01c0eaf7b6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cHJvZmlsZXxlbnwwfHwwfHw%3D&w=1000&q=80", mongo)
    josueP=Profile.create_profile('josueestr', 4.75, 20,"https://images.unsplash.com/photo-1594751543129-6701ad444259?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZGFyayUyMHByb2ZpbGV8ZW58MHx8MHx8&w=1000&q=80" , mongo)
    kevinP=Profile.create_profile('kevilin', 4.50, 4,"https://i.etsystatic.com/15418561/c/2250/1788/0/230/il/f06c80/3233862560/il_340x270.3233862560_jwqd.jpg" , mongo)
    # collection.update({'username':'victorandresvega'},{'$push':{'user_items':victorItem1.to_json()}})
    # collection.update({'username':'victorandresvega'},{'$push':{'user_items':victorItem2.to_json()}})
    # collection.update({'username':'kevilin'},{'$push':{'user_items':kevinItem1.to_json()}})
    # collection.update({'username':'kevilin'},{'$push':{'user_items':kevinItem2.to_json()}})
    # collection.update({'username':'josueestr'},{'$push':{'user_items':josueItem1.to_json()}})
    for item in mongo.db.items.find():
        username=item['username']
        user=all_users[username]
        Profile.Add_Item_to_SellDb(username,Item(item['name'],item['price'],item['size'],item['style'],item['gender'],item['description'],item['image'],user),mongo)

    
    # victorP.Add_Item_to_Sell(victorItem1)
    # victorP.Add_Item_to_Sell(victorItem2)
    # kevinP.Add_Item_to_Sell(kevinItem1)
    # kevinP.Add_Item_to_Sell(kevinItem2)
    # josueP.Add_Item_to_Sell(josueItem1)

    return 'Seeded succesfuly'

