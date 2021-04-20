
import math
import os
from dotenv import load_dotenv

load_dotenv()

from .customer import Customer

class Distance:
     def __init__(self):
        self._control_customer = Customer() 
        self._varying_customer = Customer()
        self._central_angle_radians = 0 
        self._distance_kilometres = 0
        self.distance_miles = 0
        self._longitudes_abs_diff = 0
        self._central_angle_degrees = 0
        self._distance_miles = 0
        self.setEnvironmentVariables()

    # all getter setter and deleter functions for distance_kilometres
     # getter function
     @property
     def distance_kilometres(self):
         return self._distance_kilometres
       
     # setter function
     @distance_kilometres.setter
     def distance_kilometres(self, a):
         self._distance_kilometres = a
    
    # all getter setter and deleter functions for distance_miles
     # getter function
     @property
     def distance_miles(self):
         return self._distance_miles
       
     # setter function
     @distance_miles.setter
     def distance_miles(self, a):
         self._distance_miles = a
    
    
    # all getter setter and deleter functions for _control_customer
     # getter function
     @property
     def control_customer(self):
         return self._control_customer
       
     # setter function
     @control_customer.setter
     def control_customer(self, a):
         self._control_customer = a
    
    # all getter setter and deleter functions for _varying_customer
     # getter function
     @property
     def varying_customer(self):
         return self._varying_customer
       
     # setter function
     @varying_customer.setter
     def varying_customer(self, a):
         self._varying_customer = a
    
     # deleter function
     @varying_customer.deleter
     def varying_customer(self):
         del self._varying_customer

     # all getter setter and deleter functions for longitudes_abs_diff
     # getter function
     @property
     def longitudes_abs_diff(self):
         return self._longitudes_abs_diff
       
     # setter function
     @longitudes_abs_diff.setter
     def longitudes_abs_diff(self, a):
         self._longitudes_abs_diff = a
    
     # all getter setter and deleter functions for central_angle_radians
     # getter function
     @property
     def central_angle_radians(self):
         return self._central_angle_radians
       
     # setter function
     @central_angle_radians.setter
     def central_angle_radians(self, a):
         self._central_angle_radians = a
    
    # all getter setter and deleter functions for central_angle_degrees
     # getter function
     @property
     def central_angle_degrees(self):
         return self._central_angle_degrees
       
     # setter function
     @central_angle_degrees.setter
     def central_angle_degrees(self, a):
         self._central_angle_degrees = a
     
     def get_DEGREES_IN_RADIAN(self):
         return self.DEGREES_IN_RADIAN

     def get_MEAN_EARTH_RADIUS_KM(self):
         return self.MEAN_EARTH_RADIUS_KM

     def get_KILOMETRES_IN_MILE(self):
         return self.KILOMETRES_IN_MILE

     def calculate(self):
        """
        Central method to set calculated attributes, which it
        does by calling other private functions.
        """
        #print(self.control_customer.valid)
        #print(self.varying_customer.valid)
        if self.control_customer.valid and self.varying_customer.valid:
            self.calculate_longitude_abs_diff()
            self.calculate_central_angle()
            self.calculate_central_angle_degrees()
            self.calculate_distance_km()
            self.calculate_distance_miles()
    
     def setEnvironmentVariables(self):
         """
          To prevent errors being splattered all around, we handle a case environment variables were not set
         """
         try:
             self.DEGREES_IN_RADIAN = float(os.getenv("DEGREES_IN_RADIAN"))
             self.MEAN_EARTH_RADIUS_KM = float(os.getenv("MEAN_EARTH_RADIUS_KM"))
             self.KILOMETRES_IN_MILE = float(os.getenv("KILOMETRES_IN_MILE"))
         except:
             self.DEGREES_IN_RADIAN = -1
             self.MEAN_EARTH_RADIUS_KM = -1
             self.KILOMETRES_IN_MILE = -1
    
     def calculate_longitude_abs_diff(self):
         """
         Calculate the difference between the 2 longitude's rads
         """
         self.longitudes_abs_diff = self.control_customer.longitude_radians - self.varying_customer.longitude_radians if (self.control_customer.longitude_radians > self.varying_customer.longitude_radians) else self.varying_customer.longitude_radians - self.control_customer.longitude_radians 

     def calculate_central_angle(self):
         """
         Calculate the central angle
         between two points on the surface of a sphere.
         """
         self.central_angle_radians = math.acos( math.sin(self.control_customer.latitude_radians)
                                         * math.sin(self.varying_customer.latitude_radians)
                                         + math.cos(self.control_customer.latitude_radians)
                                         * math.cos(self.varying_customer.latitude_radians)
                                         * math.cos(self.longitudes_abs_diff))

     def calculate_central_angle_degrees(self):
        """
        Calculate the central angle degrees variant of the radian
        """
        self.central_angle_degrees = self.central_angle_radians * self.DEGREES_IN_RADIAN

     def calculate_distance_km(self):

        """
        Because we are using radians, this is a simple formula multiplying the radius
        by the angle, the actual units used being irrelevant.
        """
        self.distance_kilometres = self.MEAN_EARTH_RADIUS_KM * self.central_angle_radians
        self.distance_miles = self.distance_kilometres / self.KILOMETRES_IN_MILE 
    
     def calculate_distance_miles(self):

        """
        Also the distance in miles is calculated from kilometres.
        """
        self.distance_miles = self.distance_kilometres / self.KILOMETRES_IN_MILE 


    