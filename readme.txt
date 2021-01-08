This task done using django rest framework

1.Set up your virtual environment
2.Activate virtual environment
3.In terminal run the following command
pip -r requirements.txt

this will install all the necessary package to run the system

4.One the requirements are installed then run the server using
python manage.py runserver

Import this on postman to get postman collection
POST MAN COLLECTION LINK : https://www.getpostman.com/collections/2c01b3f52e664e9ebef9

LIST OF API USED:
-----------------

0) Load the products shown in the below excel using any excel reader library (or your own custom reader) of your choice
POST ---> http://127.0.0.1:8000/read/

1) Given a product name or product code, find the top-most parent of it by its name.
GET --->http://127.0.0.1:8000/read/?option=1&name=AGNES

2) Given a product name, display the name of all of its children in sorted order.
GET --->http://127.0.0.1:8000/read/?option=2&name=AGNES

3) Display a count of active and in-active products.
GET --->http://127.0.0.1:8000/read/?option=3

4) Display the value of average product price per Category L1 and Category L2
GET --->http://127.0.0.1:8000/read/?option=4