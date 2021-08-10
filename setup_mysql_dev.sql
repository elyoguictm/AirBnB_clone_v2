--prepares a MySQL server for the project
--A database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
--A new user hbnb_dev (in localhost)
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--hbnb_dev should have SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
