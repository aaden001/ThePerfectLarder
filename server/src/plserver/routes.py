from plserver import app
from .database import Database

from flask import request

import json

db = Database()

@app.route('/')
@app.route('/index')
def index():
	return "I am a placeholder. Watch me hold places."

@app.route('/login', methods = ['POST'])
def login():
    return db.login(request.get_json())

@app.route('/signUp', methods = ['POST'])
def signUp():
	return db.signUp(request.get_json())
    
@app.route('/addItem', methods = ['POST'])
def addItem():
    return db.addItem(request.get_json())

@app.route('/getItem', methods = ['POST'])
def getItem():
    return db.getItem(request.get_json())
    
@app.route('/delItem', methods = ['POST'])
def delItem():
    return db.delItem(request.get_json())

@app.route('/getInventory', methods = ['POST'])
def getInventory():
    return db.getInventory(request.get_json())
    
@app.route('/searchItem', methods = ['POST'])
def searchItem():
    return db.searchItem(request.get_json())

@app.route('/getReccRecipes', methods = ['POST'])
def getReccRecipes():
    return db.getReccRecipes(request.get_json())

@app.route('/addRecipe', methods = ['POST'])
def addRecipe():
    return db.addRecipe(request.get_json())

@app.route('/delRecipe', methods = ['POST'])
def delRecipe():
    return db.delRecipe(request.get_json())
    
@app.route('/getPersonalRecipes', methods = ['POST'])
def getPersonalRecipes():
    return db.getPersonalRecipes(request.get_json())

@app.route('/updatePersonalRecipe', methods=['POST'])
def updatePersonalRecipe():
    return db.updatePersonalRecipe(request.get_json())

@app.route('/getItemsAboutToExpire', methods = ['POST'])
def getItemsAboutToExpire():
	return db.getItemsAboutToExpire(request.get_json())

@app.route('/getTrends', methods = ['POST'])
def getTrends():
    return db.getTrends(request.get_json())
    
@app.route('/getPerfectLarder', methods = ['POST'])
def getPerfectLarder():
    return db.getPerfectLarder(request.get_json())
    
@app.route('/getShoppingList', methods = ['POST'])
def getShoppingList():
    return db.getShoppingList(request.get_json())
    
@app.route('/updateMeasurementSetting', methods = ['POST'])
def updateMeasurementSetting():
    return db.updateMeasurementSetting(request.get_json())
    
@app.route('/updateStorageLocations', methods = ['POST'])
def updateStorageLocations():
    return db.updateStorageLocations(request.get_json())
   
@app.route("/displayAllSharedUser",methods = ["POST"])
def displayAllSharedUser():
	return db.displayAllSharedUser(request.get_json())

@app.route("/addToShareList",methods = ["POST"])
def addToShareList():
	return db.addToShareList(request.get_json())

@app.route("/removeFromShareList",methods = ["POST"])
def removeFromShareList():
	return db.removeFromShareList(request.get_json())

@app.route("/shareFoodItemToUser",methods= ["POST"])
def shareFoodItemToUser():
	return db.shareFoodItemToUser(request.get_json())

@app.route("/viewAllNotification", methods=["POST"])
def viewAllNotification():
	return db.viewAllNotification(request.get_json())
@app.route("/rejectItem", methods=["POST"])
def rejectItem():
	return db.rejectItem(request.get_json())
@app.route("/acceptItem",methods=["POST"])
def acceptItem():
	return db.acceptItem(request.get_json())
