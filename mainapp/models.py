from django.db import models
import pymongo, dns
# Create your models here.

class FWS_DB_Helper:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://mk123:mk123@cluster0-aroko.mongodb.net/test?retryWrites=true")
        self.mydb = self.client["facultyWorkloadSystemDB"]

    def getUser(self,cId):
        users=self.mydb["users"]
        user=users.find_one({'cId':cId})
        return user

    def addUser(self,user):
        users = self.mydb["users"]
        users.insert_one(user)