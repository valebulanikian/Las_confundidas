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
('Cenicienta', 'joven', 'vestido', 'rubia', 'humana', 'mujer', 'celeste'),
('Ariel', 'joven', 'vestido', 'rojo', 'no humana', 'mujer', 'rosa'),
('Mickey Mouse', 'adulto', 'pantalones rojos', 'negro', 'ratón', 'hombre', 'rojo'),
('Elsa', 'adulto', 'vestido azul', 'rubia', 'humana', 'mujer', 'azul'),
('Simba', 'joven', 'ninguna', 'dorado', 'león', 'hombre', 'amarillo'),
('Blancanieves', 'joven', 'vestido azul', 'negro', 'humana', 'mujer', 'amarillo'),
('Aladdin', 'joven', 'chaleco rojo', 'negro', 'humana', 'hombre', 'marrón'),
('Peter Pan', 'joven', 'pantalones verdes', 'rubio', 'humana', 'hombre', 'verde'),
('Pinocho', 'niño', 'pantalones cortos de madera', 'negro', 'muñeco de madera', 'hombre', 'azul'),
('Hércules', 'adulto', 'túnica roja', 'negro', 'semidios', 'hombre', 'rojo'),
('Pato Donald', 'adulto', 'chaqueta azul', 'ninguno', 'pato', 'hombre', 'azul'),
('Goofy', 'adulto', 'chaleco naranja', 'negro', 'perro', 'hombre', 'naranja'),
('Minnie Mouse', 'adulto', 'vestido rojo', 'negro', 'ratón', 'mujer', 'rojo'),
('Pluto', 'adulto', 'ninguna', 'amarillo', 'perro', 'hombre', 'amarillo'),
('Daisy', 'adulto', 'vestido morado', 'ninguno', 'pato', 'mujer', 'violeta');

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
