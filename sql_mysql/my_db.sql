------------------------------------------------------------------------
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

------------------------------------------------------------------------
--Si es un csv
--Laberinto de la soledad, octavio paz, 1960
--Vuelta al laberinto de la soledad, octavio paz 1970
--ES POSIBLE AHCER QUERYS A OTRAS TABLAS 
INSERT INTO books(tittle, author_id,) VALUES ('laberinto de la soledad',6);

INSERT INTO books (title, author_id , `year`) VALUES(
    (SELECT author_id FROM authors WHERE name = 'Sam Altman' LIMIT 1),
    'vuelta al laberinto de la soledad', 1970,'MEX');

------------------------------------------------------------------------ 
--meter esquema en mysql desde consola
--  >mysql -u root -p <all_schema.sql

--meter data en mysql desde consola
  --mysql -u root -p -D pruebaplatzi < all_data.sql

------------------------------------------------------------------------
--SELECT -> crea una tabla dinamica que solo existira en un momento
--SELECT name, email, gender FROM clients -> trae tuplas
--SELECT name, email, gender FROM clients limit 10 -> trae 10  tuplas aleatorias
--SELECT name, email, gender FROM clients where gender = 'M' -> trae tuplas de hombres
--select year(birthdate) from clients; -> trae el año de las fechas

-- SELECT NOW(); -> Traw fecha hoy del pc
-- SELECT YEAR(NOW()); Trae el año del pc
-- SELECT YEAR(now()) - YEAR(birthdate) from clients limit 10; -> edad de los clientes
---SELECT name,  YEAR(now()) - YEAR(birthdate) from clients limit 10;
-- SELECT * from clients where name like '%saave%'; -trae nombres  que tengan saave

--SELECT name AS Nombre , email AS Email, YEAR(NOW()) - YEAR(birthdate) AS Edad,
   -- gender FROM clients WHERE gender = 'F' AND  name LIKE '%Garci%'; 
    --> trae nombre de una mujer que tenga garci, con su correo y edad, tambien modifico el nombre de columnas


