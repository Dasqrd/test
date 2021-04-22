# Class primarily loads customer data from external resource
import pandas as pd
from pandas.io.json import json_normalize 
import json
from collections import namedtuple
from .customer import Customer
import os
from dotenv import load_dotenv

load_dotenv()

#Change className to LoadData
 #1 Class to Load the data from the internet
 #2 Class to handle sorting of Customer object 
 #3
class LoadData:
     def __init__(self):
          self._url = ""
          self._customer_data=[] #List to hold all customer object for me
          self._raw_data = ""
          self._error = True
          self.setEnvironmentVariables()

    
    # all getter setter and deleter functions for url
     # getter function
     @property
     def url(self):
         return self._url
       
     # setter function
     @url.setter
     def url(self, a):
         self._url = a
    
    # all getter setter and deleter functions for Customer Data
     # getter function
     @property
     def customer_data(self):
         return self._customer_data
       
     # setter function
     @customer_data.setter
     def customer_data(self, a):
         self._customer_data.append(a) 
     
     def overwrite_customer_data(self,a):
          self._customer_data = a
     # all getter setter and deleter functions for raw_data
     # getter function
     @property
     def raw_data(self):
         return self._raw_data
       
     # setter function
     @raw_data.setter
     def raw_data(self, a):
         self._raw_data = a
     
     # all getter setter and deleter functions for error
     # getter function
     @property
     def error(self):
         return self._error
       
     # setter function
     @error.setter
     def error(self, a):
         self._error = a

     def setEnvironmentVariables(self):
         """
          To prevent errors being splattered all around, we handle a case environment variables were not set
         """
         try:
             self.url = str(os.getenv("URL"))
         except:
             self.url = -1
    
     def loadExternalData(self):
         try:
            self.raw_data = pd.read_json(self.url, lines=True)
            self.error = False
         except:
            self.error = True
          
         #student = json.loads(data.to_json(), object_hook=self.customStudentDecoder())
         #
     def main(self,data):
         if data == "":
            self.loadExternalData()
         else:
            self.loadExternalDataPredefined(data)
         self.populateCustomerDataList()
         self.sortCustomerData()

     def loadExternalDataPredefined(self,data):
         try:
            self.raw_data = pd.read_json(data, lines=True)
            #print(self.raw_data.to_json())
            self.error = False
         except:
            self.error = True
          
         #student = json.loads(data.to_json(), object_hook=self.customStudentDecoder())
         #
         

     def populateCustomerDataList(self):
         if (self.error):
             return
          #next we try to parse it into a Customers object to ease calls 
         for index, row in self.raw_data.iterrows():
             thisCustomer = Customer()
             thisCustomer.latitude = row['latitude']
             thisCustomer.longitude = row['longitude']
             thisCustomer.name = row['name']
             thisCustomer.user_id = row['user_id']
             thisCustomer.calculate()
             self.customer_data.append(thisCustomer)
    
     def sortCustomerData(self):
         if (self.error):
             return
         sortedList = sorted(self._customer_data, key=lambda customer: customer.user_id, reverse=False)
         self.overwrite_customer_data(sortedList)