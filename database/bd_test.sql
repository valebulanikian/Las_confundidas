-- CREAR BASE DE DATOS
CREATE DATABASE IF NOT EXISTS personajes_test;

-- USAR BASE DE DATOS
USE personajes_test;

-- CREAR TABLA DE PERSONAJES
CREATE TABLE IF NOT EXISTS pj (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    edad VARCHAR(20),
    ropa VARCHAR(255),
    pelo VARCHAR(255),
    raza VARCHAR(255),
    genero VARCHAR(10),
    color VARCHAR(20)
);

-- INSERTAR DATOS EN LA TABLA
INSERT INTO pj (nombre, edad, ropa, pelo, raza, genero, color) VALUES
('Cenicienta', 'joven', 'vestido', 'rubio', 'humano', 'mujer', 'celeste'),
('Ariel', 'joven', 'vestido', 'rojo', 'no humano', 'mujer', 'rosa'),
('Mickey Mouse', 'adulto', 'pantalones', 'negro', 'no humano', 'hombre', 'rojo'),
('Elsa', 'adulto', 'vestido', 'rubio', 'humano', 'mujer', 'azul'),
('Simba', 'joven', 'ninguna', 'rubio', 'no humano', 'hombre', 'amarillo'),
('Blancanieves', 'joven', 'vestido', 'negro', 'humano', 'mujer', 'amarillo'),
('Aladdin', 'joven', 'chaleco', 'negro', 'humano', 'hombre', 'marrón'),
('Peter Pan', 'joven', 'pantalones', 'rubio', 'humano', 'hombre', 'verde'),
('Pinocho', 'niño', 'pantalones', 'negro', 'no humano', 'hombre', 'azul'),
('Hércules', 'adulto', 'túnica roja', 'negro', 'no humano', 'hombre', 'rojo'),
('Pato Donald', 'adulto', 'chaleco', 'ninguno', 'no humano', 'hombre', 'azul'),
('Goofy', 'adulto', 'chaleco', 'negro', 'no humano', 'hombre', 'naranja'),
('Minnie Mouse', 'adulto', 'vestido', 'negro', 'no humano', 'mujer', 'rojo'),
('Pluto', 'adulto', 'ninguna', 'amarillo', 'no humano', 'hombre', 'amarillo'),
('Daisy', 'adulto', 'vestido', 'ninguno', 'no humano', 'mujer', 'violeta');

-- SELECCIONAR TODOS LOS DATOS DE LA TABLA DE PERSONAJES
SELECT * FROM pj;

-- CREAR TABLA DE PREGUNTAS
CREATE TABLE IF NOT EXISTS preguntas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pregunta VARCHAR(200)
);

-- INSERTAR DATOS EN LA TABLA DE PREGUNTAS
INSERT INTO preguntas (pregunta) VALUES 
('¿En qué rango de edad se encuentra tu personaje?'), 
('¿Qué tipo de ropa usa?'), 
('¿Es de raza humana?'),
('¿Es una mujer?'),
('¿Qué color representa mejor a tu personaje?');

-- SELECCIONAR TODOS LOS DATOS DE LA TABLA DE PREGUNTAS
SELECT * FROM preguntas;

-- EJEMPLO DE CONSULTA CON JOIN (SI ES NECESARIO)
-- SELECT pj.ropa, preguntas.pregunta FROM pj, preguntas WHERE preguntas.id = 2 GROUP BY pj.ropa;
