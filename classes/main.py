
#Change className to Main
 #1 Class to handle all the main function of the program
 #2 Class to handle sorting of Customer object 
 #3

from .load_data import LoadData
from .customer import Customer
from .distance import Distance
import os
from dotenv import load_dotenv

load_dotenv()

class Main:
     def __init__(self):
         self.distance = Distance()
         self._customer_data=[] #List to hold all sorted customer object for me
         self.dinner_list=[] #List to hold all sorted customer object for me
         self._raw_data = ""
         self._controlCustomer = []
         self.setEnvironmentVariables()
     
     # all getter setter and deleter functions for Customer Data
     # getter function
     @property
     def customer_data(self):
         return self._customer_data
       
     # setter function
     @customer_data.setter
     def customer_data(self, a):
         self._customer_data = a
    
     # all getter setter and deleter functions for Raw Data (for default/preknown data)
     # getter function
     @property
     def raw_data(self):
         return self._raw_data
       
     # setter function
     @raw_data.setter
     def raw_data(self, a):
         self._raw_data = a
    
     # all getter setter and deleter functions for Control Customer
     # getter function
     @property
     def controlCustomer(self):
         return self._controlCustomer

     def setEnvironmentVariables(self):
         """
          To prevent errors being splattered all around, we handle a case environment variables were not set
         """
         try:
             self.DISTANCE_CHECK = float(os.getenv("DISTANCE_CHECK"))
             self.OFFICE_LATITUDE =  float(os.getenv("OFFICE_LATITUDE"))
             self.OFFICE_LONGITUDE = float(os.getenv("OFFICE_LONGITUDE"))
             self.OFFICE_NAME =str(os.getenv("OFFICE_NAME"))
         except:
             self.DISTANCE_CHECK = -1
             self.OFFICE_LATITUDE =  -1000
             self.OFFICE_LONGITUDE = -1000
             self.OFFICE_NAME =-1

       
     # setter function
     @controlCustomer.setter
     def controlCustomer(self, a):
         self._controlCustomer = a

     def setOfficeDefaults(self):
         """
            The control customer was defined as the head office since all other varying customers (loaded customers) will be compared to it 
         """
         self.controlCustomer = Customer()
         self.controlCustomer.latitude =  self.OFFICE_LATITUDE
         self.controlCustomer.longitude = self.OFFICE_LONGITUDE
         self.controlCustomer.name = self.OFFICE_NAME
         self.controlCustomer.user_id = -1
         self.controlCustomer.calculate()
         self.distance.control_customer = self.controlCustomer
     
     def setDistanceControlCustomer(self):
         self.distance.control_customer = self.controlCustomer
     
     def main_function(self):
         self.setOfficeDefaults()
         self.load_and_set_all_sorted_customer_data()
         if(self.load_data.error):
            return
         self.findDinnerList()
         self.outputToAFile(self.getOutput())

     def byeMessage(self):
         message = "No Environment File found" if self.OFFICE_LATITUDE == -1000 or self.OFFICE_LONGITUDE == -1000 else "Error while loading "+str(os.getenv("URL"))
         return message if(self.load_data.error) else "Result should be in output.txt"

    
     def load_and_set_all_sorted_customer_data(self):
         self.load_data = LoadData()
         self.load_data.main(self.raw_data)
         self.customer_data = self.load_data.customer_data

     def findDinnerList(self):
         for eachCustomer in self.customer_data:
            self.distance.varying_customer = eachCustomer
            self.distance.calculate()
            eachCustomer.distance_to_control = self.distance.distance_kilometres
            if(self.distance.distance_kilometres <= self.DISTANCE_CHECK):
                self.dinner_list.append(eachCustomer)
    
     def getOutput(self):
         index=1
         data = "---------LIST OF CUSTOMERS INVITED FOR DINNER--------\n"
         for eachCustomer in self.dinner_list:
                i=str(index)
                data+=("-----Start Customer #"+i+" -------\n"+
                str(eachCustomer)+
                "\n-----End Customer #"+i+"-------\n"
                )
                index+=1
         return data

     def outputToAFile(self,data):
         file1 = open("output.txt","w")
         file1.writelines(data)
         file1.close() 



     
