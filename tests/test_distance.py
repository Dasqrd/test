import sys
sys.path.append("..")
import unittest
from classes.customer import Customer
from classes.distance import Distance



class TestDistance(unittest.TestCase):
    """
        Test will focus on only attributes consumed by the Distance class
    """
    def set_default_values(self):
        self.controlData = Customer()
        self.controlData.latitude = 28.426846
        self.controlData.user_id = 1000
        self.controlData.name = "Control Customer's Location"
        self.controlData.longitude = 77.088834
        self.controlData.calculate()

        self.varyingData = Customer()
        self.varyingData.latitude = 28.394231
        self.varyingData.user_id = 1001
        self.varyingData.name = "Varying Customer's Location"
        self.varyingData.longitude = 77.050308
        self.varyingData.calculate()

        self.distance  = Distance()
        self.distance.control_customer = self.controlData
        self.distance.varying_customer = self.varyingData
        self.distance.calculate_longitude_abs_diff()
        self.distance.calculate_central_angle()
        self.distance.calculate_central_angle_degrees()
        self.distance.calculate_distance_km()
        self.distance.calculate_distance_miles()

    def test_DEGREES_IN_RADIAN(self):
        """
        Test to DEGREES_IN_RADIAN value  
        """
        self.set_default_values()
        self.assertEqual(self.distance.get_DEGREES_IN_RADIAN(), 57.29577951)

    def test_MEAN_EARTH_RADIUS_KM(self):
        """
        Test to MEAN_EARTH_RADIUS value  
        """
        self.set_default_values()
        self.assertEqual(self.distance.get_MEAN_EARTH_RADIUS_KM(), 6371)
    
    def test_KILOMETRES_IN_MILE(self):
        """
        Test to KILOMETRES_IN_MILE value  
        """
        self.set_default_values()
        self.assertEqual(self.distance.get_KILOMETRES_IN_MILE(), 1.60934)

    def test_varying_customer_lattitude_longitude_validity(self):
        """
        Test to confirm if varying customer_lattitude_longitude_ is valid
        """
        self.set_default_values()
        self.assertEqual(self.distance.varying_customer.valid, True)

    def test_control_customer_latitude_longitude_validity(self):
        """
        Test to confirm if control customer_lattitude_longitude_ is valid
        """
        self.set_default_values()
        self.assertEqual(self.distance.control_customer.valid, True)
    
    def test_control_customer_latitude_radians(self):
        """
        Test to confirm if control_customer_latitude_radians is 0.496142
        """
        self.set_default_values()
        self.assertEqual(float("{:.6f}".format(self.distance.control_customer.latitude_radians)), 0.496142)
    
    def test_control_customer_longitude_radians(self):
        """
        Test to confirm if control_customer_longitude_radians 1.345454
        """
        self.set_default_values()
        self.assertEqual(float("{:.6f}".format(self.distance.control_customer.longitude_radians)), 1.345454)

    def test_varying_customer_latitude_radians(self):
        """
        Test to will  
        """
        self.set_default_values()
        self.assertEqual(float("{:.6f}".format(self.distance.varying_customer.latitude_radians)), 0.495573)
    
    def test_varying_customer_longitude_radians(self):
        """
        Test to will  
        """
        self.set_default_values()
        self.assertEqual(float("{:.6f}".format(self.distance.varying_customer.longitude_radians)), 1.344782)

    def test_longitude_absolute_difference(self):
        """
        Test to longitudes_abs_diff attribute  
        """
        self.set_default_values()
        self.assertEqual(float("{:.6f}".format(self.distance.longitudes_abs_diff)), 0.000672)
    
    def test_central_angle_radians(self):
        """
        Test to longitudes_abs_diff attribute  
        """
        self.set_default_values()
        self.assertEqual(float("{:.6f}".format(self.distance.central_angle_radians)), 0.000821)
    
    def test_central_angle_degrees(self):
        """
        Test to longitudes_abs_diff attribute  
        """
        self.set_default_values()
        self.assertEqual(float("{:.6f}".format(self.distance.central_angle_degrees)), 0.047032)
    
    def test_distance_in_km(self):
        """
        Test to validate the right distance was gotten 
        """
        self.set_default_values()
        self.assertEqual(float("{:.6f}".format(self.distance.distance_kilometres)), 5.229706)
    
    def test_distance_in_miles(self):
        """
        Test to validate the right distance was gotten 
        """
        self.set_default_values()
        self.assertEqual(float("{:.2f}".format(self.distance.distance_miles)),3.25)



if __name__ == '__main__':
    unittest.main()   

