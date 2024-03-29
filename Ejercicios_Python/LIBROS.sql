DROP SCHEMA IF EXISTS LIBROS;
CREATE SCHEMA IF NOT EXISTS LIBROS;
USE LIBROS;

CREATE TABLE autor (
  ID int NOT NULL AUTO_INCREMENT primary key,
  NOMBRE varchar(256) NOT NULL
);

CREATE TABLE libro (
  ID int NOT NULL AUTO_INCREMENT primary key,
  NOMBRE varchar(256) NOT NULL,
  ISBN varchar(256) NOT NULL unique,
  ID_AUTOR int DEFAULT NULL,
  ANIO_PUBLICACION int NOT NULL DEFAULT '2000',
  FOREIGN KEY (ID_AUTOR) REFERENCES autor(ID) 
			ON DELETE CASCADE ON UPDATE SET NULL,
  CONSTRAINT ANIO_VALIDO CHECK 
				(ANIO_PUBLICACION between 1000 and 2200)
);

INSERT INTO autor (NOMBRE)
VALUES
("ISAAC ASIMOV"),
("PHILIP K. DICK"),
("RAY BRADBURY");

INSERT INTO libro (NOMBRE, ISBN, ID_AUTOR, ANIO_PUBLICACION)
VALUES
('FUNDACIÓN', '12546', '1', '1970'),
('EL HOMBRE EN EL CASTILLO', '12346', NULL, '1960'),
('FARENHEIT 451', '12586', '3', '1953');

