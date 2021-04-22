# test
Test...
=======
To be able to run this project successfuly, you must have the following packages (contained in requirements.txt generated with pipreqs --force):

1. python-dotenv
2. Panda

The command pip install -r requirements.txt should install these dependencies.

You must also have a .env file which will contain the following environment variables:
1. URL= A url with json formatted data in the format: {"latitude": "XX.XXXXXX", "user_id": XX, "name": "XXX XXXX", "longitude": "x.xxxxxx"}, each on separate lines.
2. DISTANCE_CHECK= The distance you want to check if all data in the url are within e.g 100.00
3. DEGREES_IN_RADIAN = Constant approximately 57.29577951
4. MEAN_EARTH_RADIUS_KM = Constant approximately 6371
5. KILOMETRES_IN_MILE =  Constant approximately 1.60934
6. OFFICE_LATITUDE= THis is the latitude of the control location in the format XX.XXXXX
7. OFFICE_LONGITUDE= THis is the longitude of the control location in the format XX.XXXXX
8. OFFICE_NAME = THis is the name of the office which can be any string e.g. Head Office

To run the test files, from the root folder run 
python -m unittest discover -s tests
