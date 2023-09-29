/*CREATE DATABASE discord;
USE discord; 

CREATE TABLE user(
	id_user INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
	password_username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    profile_img VARCHAR(255),
    country VARCHAR(100),
    phone VARCHAR(50), 
    birthdate DATE
)ENGINE = InnoDB; 

CREATE TABLE server(
	id_server INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    servername VARCHAR(50) NOT NULL,
    description_server TEXT,
    creation_date TIMESTAMP DEFAULT NOW()
)ENGINE = InnoDB;  

CREATE TABLE channel(
	id_channel INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    chaneel_name VARCHAR(50) NOT NULL,
    description_channel TEXT,
    id_server INT NOT NULL,
    CONSTRAINT id_server FOREIGN KEY (id_server)
		REFERENCES server (id_server)
)ENGINE = InnoDB; 

CREATE TABLE user_server(
	id_user_server INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_user INT NOT NULL,
    id_server INT NOT NULL,
    CONSTRAINT id_user_fk FOREIGN KEY (id_user)
		REFERENCES user (id_user),
	CONSTRAINT id_server_fk FOREIGN KEY (id_server)
		REFERENCES server (id_server)
)ENGINE = InnoDB;

CREATE TABLE message(
	id_message INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    content TEXT,
    creation_message TIMESTAMP NOT NULL DEFAULT NOW(),
    id_user INT NOT NULL,
    id_channel INT NOT NULL,
    CONSTRAINT id_user FOREIGN KEY (id_user)
		REFERENCES user (id_user),
	CONSTRAINT id_channel_fk FOREIGN KEY (id_channel)
		REFERENCES channel (id_channel)
)ENGINE = InnoDB;  */