import sys
sys.path.append("..")
import unittest
from classes.customer import Customer
from classes.main import Main


class TestMain(unittest.TestCase):
    def set_default_values(self):
        self.testMain = Main()
        self.setTestControlDefaults()
        self.testMain.setDistanceControlCustomer()
        self.testMain.raw_data = ('{"latitude": "39.7645187", "user_id": 12, "name": "Denver", "longitude": "-104.9951948"}\n'+
'{"latitude": "25.7825453", "user_id": 1, "name": "Miami", "longitude": " -80.2994985"}\n'+
'{"latitude": "41.8339037", "user_id": 2, "name": "Chicago", "longitude": "-87.8720471"}\n')
        self.testMain.DISTANCE_CHECK = 2000
    
    def setTestControlDefaults(self):
         """
            The test control customer was defined as the test head office since all other varying customers (loaded customers) will be compared to it 
            Loaded with New York's coordinates
         """
         self.controlCustomer = Customer()
         self.controlCustomer.latitude =  40.6976637
         self.controlCustomer.longitude = -74.1197643
         self.controlCustomer.name ="Test Head Office"
         self.controlCustomer.user_id = -1
         self.controlCustomer.calculate()
         self.testMain.controlCustomer = self.controlCustomer
    
    def test_control_customer_details(self):
        """
        Test to validate Control Customer's details were correctly loaded
        """
        self.set_default_values()
        self.assertEqual(self.testMain.controlCustomer.latitude, 40.6976637) 
    
    def test_control_customer_details_distance(self):
        """
        Test to validate Control Customer's details were correctly loaded into the distance object
        """
        self.set_default_values()
        self.assertEqual(self.testMain.distance.control_customer.latitude, 40.6976637) 
    
    def test_customer_data(self):
        """
        Test to validate all raw_data were properly parsed and saved
        """
        self.set_default_values()
        self.testMain.load_and_set_all_sorted_customer_data()
        self.assertEqual(self.testMain.load_data.countCustomerData(), 3) 
    
    def test_customer_data_sorted(self):
        """
        Test to validate all raw_data were properly sorted
        """
        self.set_default_values()
        self.testMain.load_and_set_all_sorted_customer_data()
        self.assertEqual(self.testMain.customer_data[0].user_id, 1)

    def test_DISTANCE_CHECK(self):
        """
        Test to validate all raw_data were properly sorted
        """
        self.set_default_values()
        self.assertEqual(self.testMain.DISTANCE_CHECK, 2000)

    def test_DINNER_LIST(self):
        """
        Test to validate only those customers within 2000Km were invited (Miami and Chicago)
        """
        self.set_default_values()
        self.testMain.load_and_set_all_sorted_customer_data()
        self.testMain.findDinnerList()
        self.assertEqual(len(self.testMain.dinner_list), 2)

    def test_program_output(self):
        """
        Test to validate the program output
        """
        self.set_default_values()
        self.testMain.load_and_set_all_sorted_customer_data()
        self.testMain.findDinnerList()
        self.assertEqual(self.testMain.getOutput(), "---------LIST OF CUSTOMERS INVITED FOR DINNER--------\n-----Start Customer #1 -------\n User Id: 1\n User Name: Miami\n Latitude: 25.7825453\n Longitude: -80.2994985\n Distance to Head Office: 1754.0Km\n-----End Customer #1-------\n-----Start Customer #2 -------\n User Id: 2\n User Name: Chicago\n Latitude: 41.8339037\n Longitude: -87.8720471\n Distance to Head Office: 1155.09Km\n-----End Customer #2-------\n")
        
if __name__ == '__main__':
    unittest.main()   