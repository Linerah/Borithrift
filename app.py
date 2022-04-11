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
app.config['MONGO_URI'] = "mongodb+srv://admin:naABa2nWH2J9eNzd@cluster0.vsmni.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

#Initialize PyMongo
mongo = PyMongo(app, tlsCAFile=certifi.where())

# run this the first time, to create the collection
# mongo.db.create_collection('items')
# mongo.db.create_collection('users')

# -- Session data --
app.secret_key = secrets.token_urlsafe(16)

# department set:
departments = {"Women", "Men"}

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
        user = User.get_user(username, mongo)
        if not user:
            return render_template("index.html", message="User not found")
        else:
            password = request.form['password']
            password_correct = user.compare_password(password)
            if(password_correct):
                session['username'] = request.form['username']
                return redirect('/landing') 
            else:
               return render_template("index.html", message="Incorrect password")
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        user = User.get_user(username, mongo)
        if not user:
            try:
                user = User.create_user(email, password, username, mongo)
                session['username'] = request.form['username']
                return redirect('/landing')
            except:
                return render_template("signup.html", message="Invalid email, username or password")
        elif user['email'] == email:
            return render_template("signup.html", message="Email already exists")
        else:
            return render_template("signup.html", message="Username already exists")

# LOGOUT Route
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# LANDING Route
@app.route('/landing', methods = ['GET', 'POST'])
def landing():
    if request.method == 'GET':
        items = Item.get_items(mongo)
        print(items)
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
    elif "Remove" in request.form: 
        return redirect('/remove')
    elif "Add" in request.form: 
        return redirect('/Add')
        
        
    return render_template('Profile.html',session=session,user_items=user_items,profile=profile)
@app.route('/remove',methods = ['GET', 'POST'])
def remove():

    username=session.get('username')
    collection=mongo.db.items
    profile=Profile.get_profile(username,mongo)
    if request.method == 'GET':
        user_items=list(collection.find({"username":username}))
    elif request.form["remove_item"]:
        item_to_remove=request.form["remove_item"]
        collection.remove({"name":item_to_remove})
        return redirect('/profile')
    return render_template('RemoveItem.html',session=session,user_items=user_items,profile=profile)

@app.route('/Add',methods = ['GET', 'POST'])
def Add():
    username=session.get('username')
    collection=mongo.db.items
    if request.method == 'POST':
        user = User.get_user(username, mongo)
        name=request.form["name"]
        price=float(request.form["price"])
        size=request.form["size"]
        style=request.form["style"]
        gender=request.form["gender"]
        description=request.form["description"]
        image=request.form["image_URL"]
        Item.create_item(name,price,size,style,gender,description,image,user,mongo)
        return redirect('/profile')
    return render_template('AddItem.html',session=session)



@app.route('/seed_items')
def seed_items():
    collection = mongo.db.users
    josue = User.create_user("josue@techexchange.in", "secretPassword123", "josueestr", mongo)
    kevin = User.create_user("kevin@techexchange.in", "superSecretPassword123", "kevilin", mongo)
    victor = User.create_user("victor@techexchange.in", "secretestPassword321", "victorandresvega", mongo)
    collection = mongo.db.items
    victorItem1=Item.create_item('Yosemite Tee', 15.0, 'M', 'vintage', 'Men', 'Classic T-shirt for everyday use', 'https://m.media-amazon.com/images/I/B1F9XqluwtS._CLa%7C2140%2C2000%7C818sGefkFxL.png%7C0%2C0%2C2140%2C2000%2B0.0%2C0.0%2C2140.0%2C2000.0_AC_UL1500_.png', victor, mongo)
    josueItem1=Item.create_item('Japan Tee', 25.0, 'L', 'graphic tees', 'Men', 'Japan T-shirt', 'https://media.endclothing.com/media/f_auto,q_auto:eco/prodmedia/media/catalog/product/2/3/23-02-2022_LL_UC1B4804-2-DGR_1_1.jpg', josue, mongo)
    kevinItem1=Item.create_item('Running Jacket', 55.0, 'M', 'activewear', 'Men', 'Black Jacket', 'https://images.bike24.net/i/mb/2f/75/51/nike-shield-womens-running-jacket-black-black-reflective-silver-cu3385-010-2-898743.jpg', kevin, mongo)
    victorItem2=Item.create_item('Spread Energy Tee', 20.0, 'S', 'graphic tees', 'Men', 'T-shirt to improve mood', 'https://cdn.shopify.com/s/files/1/0067/4217/9924/products/mockup-f1877084.jpg?v=1556725761', victor, mongo)
    kevinItem2=Item.create_item('Gym Jacket', 45.0, 'S', 'activewear', 'Men', 'Stylish Green Jacket, great for running', 'https://i.ebayimg.com/images/g/aw4AAOSwOVRhn8Q5/s-l400.jpg', kevin, mongo)
    collection = mongo.db.profiles
    victorP=Profile.create_profile("victorandresvega", 5.0,10,"https://images.unsplash.com/photo-1529665253569-6d01c0eaf7b6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cHJvZmlsZXxlbnwwfHwwfHw%3D&w=1000&q=80", mongo)
    josueP=Profile.create_profile('josueestr', 4.75, 20,"https://images.unsplash.com/photo-1594751543129-6701ad444259?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZGFyayUyMHByb2ZpbGV8ZW58MHx8MHx8&w=1000&q=80" , mongo)
    kevinP=Profile.create_profile('kevilin', 4.50, 4,"https://i.etsystatic.com/15418561/c/2250/1788/0/230/il/f06c80/3233862560/il_340x270.3233862560_jwqd.jpg" , mongo)
    collection.update({'username':'victorandresvega'},{'$push':{'user_items':victorItem1.to_json()}})
    collection.update({'username':'victorandresvega'},{'$push':{'user_items':victorItem2.to_json()}})
    collection.update({'username':'kevilin'},{'$push':{'user_items':kevinItem1.to_json()}})
    collection.update({'username':'kevilin'},{'$push':{'user_items':kevinItem2.to_json()}})
    collection.update({'username':'josueestr'},{'$push':{'user_items':josueItem1.to_json()}})
    for item in mongo.db.items.find():
        username=item['username']
        user = User.get_user(username, mongo)
        Profile.Add_Item_to_SellDb(username,Item(item['name'],item['price'],item['size'],item['style'],item['gender'],item['description'],item['image'],user),mongo)

    
    # victorP.Add_Item_to_Sell(victorItem1)
    # victorP.Add_Item_to_Sell(victorItem2)
    # kevinP.Add_Item_to_Sell(kevinItem1)
    # kevinP.Add_Item_to_Sell(kevinItem2)
    # josueP.Add_Item_to_Sell(josueItem1)

    return 'Seeded succesfuly'

