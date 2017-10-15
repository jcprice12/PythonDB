# PythonDB
Python 2 Text-Based DB App (Uses MySQL)

Models a retail company called "Johmpson Clothing"

Users can log in, create an account, browse products, and place orders.

Passwords are encrypted before being saved in the MySQL database.

To use the app, you need to have MySQL installed. Visit the MySQL website to install your MySQL server.
I also recommend installing the MySQL Workbench tool. It is a UI for MySQL that is really helpful for viewing data and writing SQL.
My app connedts to localhost under the username "root" and password "password". The schema I connect to is called "JohmpsonClothing".
Speaking of schemas, once you install MySQL, run the schema.sql file that is located in the "DB" folder in order to set up the database.
The schema file will also populate the database with some seed data.

You will also most likely need to install the "passlib" python module. I use this module to hash passwords with the SHA 256 algorithm.

I have been developing this app on Ubuntu version 16.04 so Python 2 already came with the OS for me. If you're using Windows, you may need to install
a lot more things.

To run the app (once everything is installed), just run the customerApp.py file in the root folder with "python customerApp.py"
