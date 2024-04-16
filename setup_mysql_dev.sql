#!/bin/bash

# Set MySQL root password
mysql -e "SET GLOBAL validate_password_policy=0; ALTER USER 'root'@'localhost' IDENTIFIED BY 'my_secure_password';"

# Create the hbnb_dev_db database
mysql -e "CREATE DATABASE IF NOT EXISTS hbnb_dev_db;"

# Create the hbnb_dev user and grant privileges
mysql -e "GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'; FLUSH PRIVILEGES;"

# Grant SELECT privilege on performance_schema to hbnb_dev
mysql -e "GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'; FLUSH PRIVILEGES;"
