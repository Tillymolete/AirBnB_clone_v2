-- script that create new user and give him some privileges
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
CREATE USER IF NOT EXISTS  `hbnb_dev`@localhost IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO `hbnb_dev`@localhost;
GRANT SELECT ON `hbnb_dev_db`.* TO `hbnb_dev`@localhost;