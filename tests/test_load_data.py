import sys
sys.path.append("..")
import unittest
from classes.customer import Customer
from classes.load_data import LoadData
import os
from dotenv import load_dotenv

load_dotenv()


class TestDistance(unittest.TestCase):
    """
        Test will focus on only attributes consumed by the LoadData class
    """
    def set_default_values(self):
        self.loadDataObject = LoadData()
        self.jsonString = ('{"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}\n'+
'{"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"}\n'+
'{"latitude": "51.8856167", "user_id": 2, "name": "Ian McArdle", "longitude": "-10.4240951"}\n')
        self.loadDataObject.loadExternalDataPredefined(self.jsonString)
        self.loadDataObject.populateCustomerDataList()
    
    def test_confirm_url(self):
        """
        Test to confirm URL value is as expected
        """
        self.set_default_values()
        self.assertEqual(self.loadDataObject.url,str(os.getenv("URL")))
    
    def test_loadExternalData(self):
        """
        Test to confirm external data was loaded from a URL
        """
        self.set_default_values()
        self.loadDataObject.loadExternalData()
        self.assertFalse(self.loadDataObject.error)


    def test_loadExternalDataPredefined(self):
        """
        Test to confirm external data was loaded from a teststring defined above
        """
        self.set_default_values()
        self.assertFalse(self.loadDataObject.error)

    def test_populateCustomerDataList(self):
        """
        Test to confirm customer Data list was rightly populated
        """
        self.set_default_values()
        self.assertEqual(self.loadDataObject.countCustomerData(),3)
    
    def test_populateCustomerDataListUnsorted(self):
        """
        Test to confirm customer Data list is not sorted at this point
        """
        self.set_default_values() 
        self.assertEqual(self.loadDataObject.customer_data[0].user_id,12)

    def test_populateCustomerDataListSorted(self):
        """
        Test to confirm customer Data list is not sorted at this point
        """
        self.set_default_values() 
        self.loadDataObject.sortCustomerData()
        self.assertEqual(self.loadDataObject.customer_data[0].user_id,1)
    

if __name__ == '__main__':
    unittest.main()  

    
        