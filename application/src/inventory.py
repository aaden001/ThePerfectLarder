# The Perfect Larder 
# Team Orange
# CS411W ODU Fall 2019
# By: Adeniyi Adeniran, Chris Whitney, Collin DeWaters, Derek Tiller, Jonathan Schneider
#     Matthew Perry, Melanie Devoe, and Zachery Miller 


#setup GUI(kivy)

import kivy
kivy.require('1.11.1')
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
import requests
import json

class Inventory(Screen):
    itemName = ObjectProperty(None)
    quantity = ObjectProperty(None)
    expirationDate = ObjectProperty(None)
    storageLocation = ObjectProperty(None)
    #userID = ObjectProperty(None) 
    items = []
    itemToDel = -1
    def on_pre_enter(self):
        self.manager.transition.direction = 'left'
        self.ids.inventoryID.clear_widgets()
        response = requests.post('http://411orangef19-mgmt.cs.odu.edu:8000/getInventory', headers={'Content-Type': 'application/json'}, data=json.dumps(dict(userID=App.get_running_app().userID))).json()
        
        if response['data'] != 'Inventory is currently empty.':
            self.items = response['data']
            for n in range(0, len(response['data'])):
                if response['data'][n]['quantity'] > 0:
                    button = Button(text = response['data'][n]['itemname'] + " - " + str(response['data'][n]['quantity']) + " " + response['data'][n]['measurement'])
                    callback = lambda n:self.delItem(n)
                    button.itemToDel = n
                    button.bind(on_press = callback)
                    self.ids.inventoryID.add_widget(button)
        else:
            self.ids.inventoryID.add_widget(Button(text = 'Inventory currently empty.'))
    
    def SearchItem(self):
        #Pulling incorrect index after search.
        key = self.ids.search.text
        
        response = requests.post('http://411orangef19-mgmt.cs.odu.edu:8000/searchItem', headers={'Content-Type': 'application/json'}, data=json.dumps(dict(userID=App.get_running_app().userID, itemname=key))).json()
        
        if response['data'] == "Item not found in inventory.":
            button = Button(text="No items matched your search.")
        else:
            self.items = response['data']
            self.ids.inventoryID.clear_widgets()
            for n in range(0, len(response['data'])):
                button = Button(text = response['data'][n]['itemname'] + " - " + str(response['data'][n]['quantity']) + " " + response['data'][n]['measurement'])
                callback = lambda n:self.delItem(n)
                button.itemToDel = n
                button.bind(on_press = callback)
                self.ids.inventoryID.add_widget(button)
        
    def delItem(self, index):
        self.itemToDel = index
        self.manager.current = 'deleteitem'
    
class AddItem(Screen):            #part of inventory

    def on_pre_enter(self):
        self.manager.transition.direction = 'left'
        if App.get_running_app().userMeasurement == 0:
            self.ids.measurement.values = ('teaspoon', 'tablespoon', 'fluid ounce(fl oz)', 'cup', 'pint', 'quart', 'gallon', 'ounce(oz)', 'pounds(lbs)', 'mL', 'liter(L)', 'gram(g)', 'unit')
        else:
            self.ids.measurement.values = ('mL', 'liter(L)', 'gram(g)')
        
    def addItems(self):
    
        #popup to confirm item was added
        nameContent = GridLayout(cols=1)
        nameContent.add_widget(Label(text= self.itemName.text + ' added to your inventory'))
        nameButton = Button(text='OK')
        nameContent.add_widget(nameButton)
        addItemPopup = Popup(title='Added Item', content=nameContent, auto_dismiss=False, size_hint=(.85, .2))
        nameButton.bind(on_press=addItemPopup.dismiss)
            
        #popup to let the user know the item was not added 
        nameContent = GridLayout(cols=1)
        nameContent.add_widget(Label(text= self.itemName.text + ' not added to your inventory'))
        nameButton = Button(text='OK')
        nameContent.add_widget(nameButton)
        itemNotaddedPopup = Popup(title='Item Not Added', content=nameContent, auto_dismiss=False, size_hint=(.85, .2))
        nameButton.bind(on_press=itemNotaddedPopup.dismiss)
            
        headers = {'Content-Type' : 'application/json'}
           
        payload = {
            'userID' : App.get_running_app().userID,
            'itemname' : self.ids.itemName.text,
            'quantity' : self.ids.quantity.text,
            'measurement' : self.ids.measurement.text,
            'expDate' : self.ids.expirationDate.text,
            'location' : self.ids.storageLocation.text
        }
            
        response = requests.post('http://411orangef19-mgmt.cs.odu.edu:8000/addItem', headers=headers, data=json.dumps(payload)).json()
        
        if response['data'] == 'Item added.':
            addItemPopup.open()
            self.clearFieldsAdd()
        else:
            self.itemNotaddedPopup.open()

    def clearFieldsAdd(self):
        self.ids.itemName.text = ""
        self.ids.quantity.text = ""
        self.ids.measurement.text = ""
        self.ids.expirationDate.text = ""
        self.ids.storageLocation.text = ""
    
class DeleteItem(Screen):        #part of inventory
    
    index = NumericProperty(None)
    
    def on_pre_enter(self):
        self.manager.transition.direction = 'left'
        invScreen = self.manager.get_screen('inventory')
        item = invScreen.items[invScreen.itemToDel.itemToDel]
        self.ids.name.text = item['itemname']
        self.ids.exp.text = str(item['expDate'])
        self.ids.quantity.text = str(item['quantity']) + " " + item['measurement']
        self.ids.loc.text = item['location']
        
    def deleteItems(self):
        
        invScreen = self.manager.get_screen('inventory')
        item = invScreen.items[invScreen.itemToDel.itemToDel]
    
        headers = {'Content-Type' : 'application/json'}

        payload = {
            'itemID' : item['itemID'],
            'quantity' : self.ids.used.text,
            'useType' : self.ids.useType.text
            }
            
        response = requests.post('http://411orangef19-mgmt.cs.odu.edu:8000/delItem', headers=headers, data=json.dumps(payload)).json()

        if response['data'] == "Item deleted.":
            self.clearFieldsDel()
            self.manager.current = "inventory"

    def clearFieldsDel(self):
        self.ids.used.text = ""
        self.ids.useType.text = ""