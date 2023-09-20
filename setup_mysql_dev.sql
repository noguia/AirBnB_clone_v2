-- script that prepares a MySQL server for the project
CREATE hbnb_dev_db IF NOT EXISTS hbnb_dev_db;
CREATE hbnb_dev IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
