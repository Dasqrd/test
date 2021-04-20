import sys
sys.path.append("..")
import unittest
from classes.customer import Customer

class TestCustomer(unittest.TestCase):
    def set_default_values(self):
        self.testData = Customer()
        self.testData.latitude = 40.6976637
        self.testData.user_id = 1000
        self.testData.name = "Test Name"
        self.testData.longitude = -74.1197643
    
    def test_DEGREES_IN_RADIAN(self):
        """
        Test to DEGREES_IN_RADIAN value  
        """
        self.set_default_values()
        self.assertEqual(self.testData.get_DEGREES_IN_RADIAN(), 57.29577951)

    def test_affirm_latitude(self):
        """
        Test to validate attributes are as they are supposed to be 
        """
        self.set_default_values()
        self.assertEqual(self.testData.latitude, 40.6976637)
    
    def test_affirm_longitude(self):
        """
        Test to validate attributes are as they are supposed to be 
        """
        self.set_default_values()
        self.assertEqual(self.testData.longitude, -74.1197643)
    
    def test_affirm_name(self):
        """
        Test to validate attributes are as they are supposed to be 
        """
        self.set_default_values()
        self.assertEqual(self.testData.name, "Test Name")
    
    def test_affirm_user_id(self):
        """
        Test to validate attributes are as they are supposed to be 
        """
        self.set_default_values()
        self.assertEqual(self.testData.user_id, 1000)
    
    def test_affirm_latitude_longitude_validity(self):
        """
        Test to validate attributes are as they are supposed to be 
        """
        self.set_default_values()
        self.testData.validate_degrees()
        self.assertEqual(self.testData.valid, True)
    
    def test_affirm_latitude_radian(self):
        """
        Test to validate attributes are as they are supposed to be 
        """
        self.set_default_values()
        self.testData.calculate_radians()
        self.assertEqual(float("{:.6f}".format(self.testData.latitude_radians)), 0.710308) #6 decimal places to cater for approxination 
    
    def test_affirm_longitude_radian(self):
        """ 
        Test to validate attributes are as they are supposed to be 
        """
        self.set_default_values()
        self.testData.calculate_radians()
        self.assertEqual(float("{:.6f}".format(self.testData.longitude_radians)), -1.293634) #6 decimal places to cater for approxination 
    

if __name__ == '__main__':
    unittest.main()