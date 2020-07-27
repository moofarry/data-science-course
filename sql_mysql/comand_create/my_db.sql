DROP DATABASE IF EXISTS pruebaplatzi;

CREATE DATABASE pruebaplatzi;
USE pruebaplatzi;

CREATE TABLE `authors` (
  `author_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `nationality` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`author_id`),
  UNIQUE KEY `uniq_author` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=193 DEFAULT CHARSET=utf8;

CREATE TABLE `books` (
  `book_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `author_id` int(10) unsigned DEFAULT NULL,
  `title` varchar(100) NOT NULL,
  `year` int(11) NOT NULL DEFAULT '1900',
  `language` varchar(2) NOT NULL COMMENT 'ISO 639-1 Language code (2 chars)',
  `cover_url` varchar(500) DEFAULT NULL,
  `price` double(6,2) DEFAULT NULL,
  `sellable` tinyint(1) NOT NULL DEFAULT '0',
  `copies` int(11) NOT NULL DEFAULT '1',
  `description` text,
  PRIMARY KEY (`book_id`),
  UNIQUE KEY `book_language` (`title`,`language`)
) ENGINE=InnoDB AUTO_INCREMENT=199 DEFAULT CHARSET=utf8;

CREATE TABLE `clients` (
  `client_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `birthdate` date DEFAULT NULL,
  `gender` enum('M','F') DEFAULT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`client_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;

CREATE TABLE `transactions` (
  `transaction_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `book_id` int(10) unsigned NOT NULL,
  `client_id` int(10) unsigned NOT NULL,
  `type` enum('lend','sell') NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `finished` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`transaction_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO authors(name, nationality) VALUES ('Juan Rulfo', 'MEX');
INSERT INTO authors(name, nationality) VALUES ('Gabriel Garciía Marquez', 'COL');
INSERT INTO authors(name, nationality) VALUES ('Juan Gabriel Vasquez', 'COL');
INSERT INTO authors(name, nationality) VALUES ('Julio Cortázar', 'ARG'),
    ('Isabel Allende', 'CHI'),
    ('Octavio', 'MEX'),
    ('Juan Carlos Onetti', 'URU');
    
INSERT INTO`clients`(client_id, name, email, birthdate, gender, active) VALUES
	(1,'Maria Dolores Gomez','Maria Dolores.95983222J@random.names','1971-06-06','F',1),
	(2,'Adrian Fernandez','Adrian.55818851J@random.names','1970-04-09','M',1),
	(3,'Maria Luisa Marin','Maria Luisa.83726282A@random.names','1957-07-30','F',1),
	(4,'Pedro Sanchez','Pedro.78522059J@random.names','1992-01-31','M',1);


--Si es un csv
--Laberinto de la soledad, octavio paz, 1960
--Vuelta al laberinto de la soledad, octavio paz 1970
--ES POSIBLE AHCER QUERYS A OTRAS TABLAS 
INSERT INTO books(tittle, author_id,) VALUES ('laberinto de la soledad',6);

INSERT INTO books (title, author_id , `year`) VALUES(
    (SELECT author_id FROM authors WHERE name = 'Sam Altman' LIMIT 1),
    'vuelta al laberinto de la soledad', 1970,'MEX');
---------------