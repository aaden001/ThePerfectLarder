# The Perfect Larder 
# Team Orange
# CS411W ODU Fall 2019
# By: Adeniyi Adeniran, Chris Whitney, Collin DeWaters, Derek Tiller, Jonathan Schneider
#     Matthew Perry, Melanie Devoe, and Zachery Miller 


# setup GUI (kivy)

import kivy

kivy.require('1.11.1')
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

import requests
import json


nameEmptyContent = GridLayout(cols=1)
nameEmptyContent.add_widget(Label(text='The username field  cannot be empty.'))
nameEmptyButton = Button(text='OK')
nameEmptyContent.add_widget(nameEmptyButton)
nameEmptyPopup = Popup(title='Empty input in Username', content=nameEmptyContent, auto_dismiss=False, size_hint=(.8, .2))
nameEmptyButton.bind(on_press=nameEmptyPopup.dismiss)
# `Profile`: Allows for account creation, editing, and deletion in the TPL server.
class Profile(Screen):

    def on_enter(self):
        pass

    # region Properties

    # The username of the authenticated user.
    username = ObjectProperty(None)

    # The authenticated user's password.
    password = ObjectProperty(None)

    # The email address of the authenticated user.
    email = ObjectProperty(None)

    # endregion

    # region Initialization

#     def __init__(self, username, password="", email=""):
#         self.username = username
#         self.password = password
#         self.email = email

    # endregion

    # TODO: Implement create user, edit user, delete user.

    # region Profile Operations

    # def createUserProfile(self):
    # send (self.userName.text, self.userPassword.text, self.userEmail.text) to database
    # self.userName.text = ""
    # self.userPassword.text = ""
    # self.userEmail.text = ""

    # def editUserProfile(self):
    # send (self.userName.text, self.userPassword.text, self.userEmail.text) to database
    # self.userName.text = ""
    # self.userPassword.text = ""
    # self.userEmail.text = ""

    # def deleteUserProfile(self):
    # send (self.userName.text, self.userPassword.text, self.userEmail.text) to database
    # self.userName.text = ""
    # self.userPassword.text = ""
    # self.userEmail.text = ""

    # endregion

#class StorageLocation(GridLayout):
#    def deleteSelf(self):
#        self.parent.remove_widget(self)
    
class Settings(Screen):
    
    def on_pre_enter(self):
        measureType = App.get_running_app().userMeasurement
        if measureType == 0:
            self.ids.imperial.state = 'down'
        else:
            self.ids.metric.state = 'down'
            
        for i in App.get_running_app().storageLocations:
            button = Button(text=i)
            self.ids.locations.add_widget(button)
            button.bind(on_press=lambda i:self.removeLocation(i))
            
    def addLocation(self):
        if self.ids.newLoc.text != "":
            loc = self.ids.newLoc.text
            button = Button(text=loc)
            self.ids.locations.add_widget(button)
            button.bind(on_press=lambda loc:self.removeLocation(loc))
            
    def removeLocation(self, location):
        #self.ids.locations.children.pop(0)
        num = 0
        for i in self.ids.locations.children:
            if i.text == location:
                self.ids.locations.children.pop(num)
                break
            else:
                num += 1
    
    def updateMeasurement(self):
        #button = 0
        #for i in ToggleButtonBehavior.get_widgets('measurements'):
        #    if i.state == 'down':
        #        button = i
        #        break
        payload = {
            'userID' : App.get_running_app().userID
        }
        if self.ids.imperial.state == 'down':
            payload['measureType'] = 0
        else:
            payload['measureType'] = 1
            
        r = requests.post('http://411orangef19-mgmt.cs.odu.edu:8000/updateMeasurementSetting', headers={'Content-Type':'application/json'}, data=json.dumps(payload)).json()
        
        if r['data'] == 'Successfully Updated.':
            self.manager.current = 'profile'
            App.get_running_app().userMeasurement = payload['measureType']


class ManagePL(Screen):  # part of the user profile
    pass


class EditCreateProfile(Screen):  # part of the user profile
    pass


class SetupEditNotification(Screen):  # part of the user profile
    pass

class SharedUser(Screen):
    def on_pre_enter(self):
    
        payload = {
        'userID': App.get_running_app().userID
        }
        r = requests.post('http://411orangef19-mgmt.cs.odu.edu:8000/displayAllSharedUser', headers={'Content-Type':'application/json'}, data=json.dumps(payload)).json()
        if(r['data'] =="empty"):
            print("No other user is currently in your share List")
        else:
            print(r['data'])
class AddUserToShareList(Screen):
    def submitUser(self):
        usersName = self.ids.usernameRecieved.text
        if(usersName != ""):
            payload ={
            'userID': App.get_running_app().userID,
            'userName': usersName
            }
            r = requests.post('http://411orangef19-mgmt.cs.odu.edu:8000/addToShareList', headers={'Content-Type':'application/json'}, data=json.dumps(payload)).json()
            print(r['data'])
            if(r['data'] == 1):
                print("That username does not exist")
            elif(r['data'] == 2):
                print("You can not add yourself to the shared List")
            elif(r['data'] == 3):
                print("The username " + userName +" has already been added to the shared List")
            else:
                print("Successfully added " + usersName +" to your shared List")
        else:
            nameEmptyPopup.open()
class DeleteSharedUser(Screen):
    def deleteUser(self):
        usersName = self.ids.usernameRecieved.text
        if(usersName != ""):
            payload ={
            'userID': App.get_running_app().userID,
            'userName': usersName
            }
            r = requests.post('http://411orangef19-mgmt.cs.odu.edu:8000/removeFromShareList', headers={'Content-Type':'application/json'}, data=json.dumps(payload)).json()
            print(r['data'])
            if(r['data'] ==1):
                print("That username does not exist")
            elif(r['data'] ==2):
                print("Invalid input your username " + usersName +" can not be in the shared list. Why delete nothing ?!")
            elif(r['data'] ==3 ):
                print("User name " + usersName + "Is  not on the list. Why delete nothing?!")
            else:
                print("Successfully deleted " + usersName +" from your shared List")
        else:
            nameEmptyPopup.open()