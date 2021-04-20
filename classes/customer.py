# Class for each Customer's properties mainly 
  
import os
from dotenv import load_dotenv

load_dotenv()

DEGREES_IN_RADIAN = float(os.getenv("DEGREES_IN_RADIAN"))


class Customer:
     def __init__(self):
          self._latitude = 0
          self._user_id = 0
          self._name = 0
          self._longitude = 0
          self._valid = False
          self._latitude_radians = 0
          self._longitude_radians = 0
          self._distance_to_control = 0

    # all getter setter and deleter functions for Distance to Control
     # getter function
     @property
     def distance_to_control(self):
         return self._distance_to_control
       
     # setter function
     @distance_to_control.setter
     def distance_to_control(self, a):
         self._distance_to_control = a
    
    # all getter setter and deleter functions for latitude
     # getter function
     @property
     def latitude(self):
         return self._latitude
       
     # setter function
     @latitude.setter
     def latitude(self, a):
         self._latitude = a
    
    
     # all getter setter and deleter functions for user_id
     # getter function
     @property
     def user_id(self):
         return self._user_id
       
     # setter function
     @user_id.setter
     def user_id(self, a):
         self._user_id = a

    # all getter setter and deleter functions for name
     # getter function
     @property
     def name(self):
         return self._name
       
     # setter function
     @name.setter
     def name(self, a):
         self._name = a

    # all getter setter and deleter functions for longitude
     # getter function
     @property
     def longitude(self):
         return self._longitude
       
     # setter function
     @longitude.setter
     def longitude(self, a):
         self._longitude = a
    
    # all getter setter and deleter functions for valid
     # getter function
     @property
     def valid(self):
         return self._valid
       
     # setter function
     @valid.setter
     def valid(self, a):
         self._valid= a

    # all getter setter and deleter functions for latitude_radians
     # getter function
     @property
     def latitude_radians(self):
         return self._latitude_radians
       
     # setter function
     @latitude_radians.setter
     def latitude_radians(self, a):
         self._latitude_radians= a

    # all getter setter and deleter functions for longitude_radians
     # getter function
     @property
     def longitude_radians(self):
         return self._longitude_radians
       
     # setter function
     @longitude_radians.setter
     def longitude_radians(self, a):
         self._longitude_radians= a
     
     def get_DEGREES_IN_RADIAN(self):
         return DEGREES_IN_RADIAN
    
     def calculate(self):
        """
        Central method to set calculated attributes, which it
        does by calling other private functions.
        """
        #print("CALCULATE Oooooooo")
        self.validate_degrees()

        if self.valid:
            self.calculate_radians()
    
     def validate_degrees(self):

        """
        Ensure latitudes and longitudes are within valid ranges.
        """
        self.valid = True

        if self._latitude < -90.0 or self._longitude > 90.0:
            self.valid = False

        if self._longitude < -180.0 or self._longitude > 180.0:
            self.valid = False

     def calculate_radians(self):
        """
        Calculate radians from degrees by dividing the values by a constant.
        """
        self._latitude_radians = self.latitude / DEGREES_IN_RADIAN
        self._longitude_radians = self.longitude / DEGREES_IN_RADIAN

     def __str__(self):
         """
         Custom function to convert Customer object to String
         """
         finalString= (" User Id: " + str(self.user_id) +
           "\n User Name: " + str(self.name) +
           "\n Latitude: " + str(self.latitude) +
           "\n Longitude: " + str(self.longitude) +
           "\n Distance to Head Office: " + str(float("{:.2f}".format(self.distance_to_control))) + "Km"
         ) 
         return finalString
    