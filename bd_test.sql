/* -- CREAR BASE DE DATOS
create database personajes_test;
*/
-- USAR BASE DE DATOS
use personajes_test;


-- CREAR TABLA DE PERSONAJES
CREATE TABLE personajes_test.pj (
    id INT NOT NULL AUTO_INCREMENT,
    ropa VARCHAR(45),
    pelo VARCHAR(45),
    raza VARCHAR(45),
    PRIMARY KEY (id)
);

-- MODIFICAR COSAS DE LA TABLA
alter table pj
add column edad varchar(20),
add column genero varchar(10), 
add column nombre varchar(20);

alter table pj
add column color varchar (20);

alter table pj
modify column nombre varchar(20) after id,
modify column edad varchar(20) after nombre;


-- INSERTAR DATOS EN LA TABLA
INSERT INTO pj (nombre, edad, ropa, pelo, raza, genero, color) VALUES
('Cenicienta', 'joven', 'vestido', 'rubia', 'humana', 'mujer', 'celeste'),
('Ariel', 'joven', 'vestido', 'rojo', 'no humana', 'mujer', 'rosa'),
('Mickey Mouse', 'adulto', 'pantalones rojos', 'negro', 'ratón', 'hombre', 'rojo'),
('Elsa', 'adulto', 'vestido azul', 'rubia', 'humana', 'mujer', 'azul'),
('Simba', 'joven', 'ninguna', 'dorado', 'león', 'hombre', 'amarillo'),
('Blancanieves', 'joven', 'vestido azul', 'negro', 'humana', 'mujer', 'amarillo'),
('Aladdin', 'joven', 'chaleco rojo', 'negro', 'humana', 'hombre', 'marrón'),
('Peter Pan', 'joven', 'pantalones verdes', 'rubio', 'humana', 'hombre', 'verde'),
('Pinocho', 'niño', 'pantalones cortos de madera', 'negro', 'muñeco de madera', 'hombre', 'azul'),
('Hércules', 'adulto', 'túnica roja', 'negro', 'semidios', 'hombre', 'rojo');

SELECT * FROM personajes_test.pj;

