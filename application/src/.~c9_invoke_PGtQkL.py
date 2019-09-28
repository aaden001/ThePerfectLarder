# The Perfect Larder 
# Team Orange
# CS411W ODU Fall 2019
# By: Adeniyi Adeniran, Chris Whitney, Collin DeWaters, Derek Tiller, Jonathan Schneider
#     Matthew Perry, Melanie Devoe, and Zachery Miller 

import kivy
import unittest
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.spinner import Spinner

from feedback import Feedback
from inventory import Inventory, AddItem, DeleteItem, ViewInventory, SearchItem
from itemshare import ItemShare
from login import Login
from notification import Notification
from recipes import Recipes, AddRecipe, GetRecipe
from settings import Settings
from shoppinglist import ShoppingList
from trends import Trends
from userprofile import Profile, ManagePL, EditCreateProfile, SetupEditNotification

Builder.load_file('kv/feedback.kv')
Builder.load_file('kv/inventory.kv')
Builder.load_file('kv/itemshare.kv')
Builder.load_file('kv/login.kv')
Builder.load_file('kv/main.kv')
Builder.load_file('kv/notification.kv')
Builder.load_file('kv/recipes.kv')
Builder.load_file('kv/settings.kv')
Builder.load_file('kv/shoppinglist.kv')
Builder.load_file('kv/trends.kv')
Builder.load_file('kv/userprofile.kv')

class HomeScreen(Screen):    # Main screen after login
    pass

screenManager = ScreenManager()
screenManager.add_widget(Login(name="userlogin"))
screenManager.add_widget(HomeScreen(name="homescreen"))
screenManager.add_widget(Profile(name="profile"))
screenManager.add_widget(Recipes(name="recipes"))
screenManager.add_widget(Inventory(name="inventory"))
screenManager.add_widget(Trends(name="trends"))
screenManager.add_widget(ShoppingList(name="shoppinglist"))
screenManager.add_widget(ItemShare(name="shareitems"))

screenManager.add_widget(ManagePL(name="managepl"))
screenManager.add_widget(EditCreateProfile(name="editcreateprofile"))
screenManager.add_widget(SetupEditNotification(name="setupeditnotification"))

screenManager.add_widget(AddRecipe(name="addrecipe"))
screenManager.add_widget(GetRecipe(name="getrecipe"))

screenManager.add_widget(AddItem(name="additem"))
screenManager.add_widget(DeleteItem(name="deleteitem"))
screenManager.add_widget(ViewInventory(name="viewinventory"))
screenManager.add_widget(SearchItem(name="searchitem"))
#screenManager.add_widget(ThePerfectLarder(name="theperfectlarder"))

#must have on start and build
class testApp (App):
    def on_start(self):
        pass
    
    def build(self):
        return screenManager
		
if __name__ == "__main__":
    testApp().run()