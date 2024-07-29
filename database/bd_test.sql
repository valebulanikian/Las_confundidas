

-- CREAR BASE DE DATOS
CREATE DATABASE IF NOT EXISTS personajes_test;

-- USAR BASE DE DATOS
USE personajes_test;

drop table pj;

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
('Daisy', 'adulto', 'vestido', 'ninguno', 'no humano', 'mujer', 'violeta'),
('Rapunzel', 'joven', 'vestido', 'rubio', 'humano', 'mujer', 'púrpura'),
('Tarzan', 'adulto', 'pantalones', 'rubio', 'no humano', 'hombre', 'verde'),
('Aurora', 'joven', 'vestido', 'rubio', 'humano', 'mujer', 'rosa'),
('Jasmine', 'joven', 'traje', 'negro', 'humano', 'mujer', 'turquesa'),
('Hada Madrina', 'adulto', 'vestido', 'gris', 'no humano', 'mujer', 'azul'),
('Beast', 'adulto', 'túnica', 'morado', 'no humano', 'hombre', 'morado'),
('Pocahontas', 'joven', 'traje', 'negro', 'humano', 'mujer', 'marrón'),
('Tiana', 'joven', 'vestido', 'negro', 'humano', 'mujer', 'verde'),
('Jafar', 'adulto', 'túnica', 'negro', 'humano', 'hombre', 'rojo'),
('Nala', 'joven', 'ninguna', 'amarillo', 'no humano', 'mujer', 'amarillo'),
('Bambi', 'niño', 'ninguna', 'marrón', 'no humano', 'hombre', 'marrón'),
('Thumper', 'niño', 'ninguna', 'gris', 'no humano', 'hombre', 'gris'),
('Dumbo', 'niño', 'ninguna', 'gris', 'no humano', 'hombre', 'gris'),
('Mowgli', 'niño', 'pantalones cortos', 'negro', 'humano', 'hombre', 'marrón'),
('Lilo', 'niño', 'vestido', 'negro', 'humano', 'mujer', 'rojo'),
('Winnie the Pooh', 'niño', 'camiseta', 'amarillo', 'no humano', 'hombre', 'amarillo'),
('Kanga', 'niño', 'ninguna', 'café', 'no humano', 'mujer', 'café');

select color from pj group by color;

select * from pj where pelo='blanco';

#Desactivar modo seguro de actualizaciones
SET SQL_SAFE_UPDATES = 0;

#Actualizar
UPDATE pj set pelo='marrón' where pelo='café';
UPDATE pj set ropa='pantalones' where ropa='pantalones cortos';
UPDATE pj set ropa='túnica' where ropa='túnica roja';
UPDATE pj set ropa='chaleco' where ropa='camiseta';
UPDATE pj set pelo='gris' where pelo='blanco';
UPDATE pj set color='violeta' where color='púrpura';
UPDATE pj set color='celeste' where color='turquesa';

 
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

use personajes_test;

CREATE TABLE IF NOT EXISTS cuentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    sinopsis VARCHAR(500) NOT NULL
);

INSERT INTO cuentos (nombre, sinopsis) VALUES
('Cenicienta', 'Cenicienta es una joven amable y bondadosa que vive con su malvada madrastra y hermanastras. Con la ayuda de su hada madrina, asiste al baile real y conquista al príncipe. A pesar de perder su zapato de cristal, el príncipe la encuentra y la lleva al palacio, donde viven felices para siempre.'),
('Blancanieves', 'Blancanieves es una princesa cuya madrastra, la Reina Malvada, celosa de su belleza, intenta matarla. Blancanieves se refugia con siete enanitos en el bosque. La Reina Malvada la engaña con una manzana envenenada, pero un príncipe la revive con un beso de amor verdadero.'),
('Aladdin', 'Aladdin es un joven ladrón que encuentra una lámpara mágica con un genio que concede tres deseos. Con la ayuda del genio, Aladdin se convierte en príncipe para ganar el amor de la Princesa Jasmine y derrotar al malvado Jafar, demostrando que el verdadero valor está en ser uno mismo.'),
('Peter Pan', 'Peter Pan es un niño que nunca crece y vive en el País de Nunca Jamás. Lleva a Wendy y a sus hermanos a vivir aventuras y enfrentar al malvado Capitán Garfio. Peter Pan enseña la importancia de la imaginación y la juventud eterna, derrotando a Garfio y regresando a sus amigos a casa.'),
('Pinocho', 'Pinocho es un muñeco de madera creado por Geppetto y traído a la vida por el Hada Azul. Para convertirse en un niño de verdad, debe demostrar ser valiente y honesto. Acompañado por el grillo Pepe, enfrenta pruebas y tentaciones, aprendiendo lecciones importantes sobre la verdad y el valor.'),
('Hercules', 'Hércules es un joven dios con fuerza sobrehumana que fue secuestrado del Olimpo y criado como mortal. Para recuperar su lugar entre los dioses, debe convertirse en un verdadero héroe. Con la ayuda de su amor Megara y su entrenador Fil, enfrenta desafíos y derrota al malvado Hades.'),
('Pato Donald', 'El Pato Donald es conocido por su temperamento explosivo y su voz distintiva. Es un amigo cercano de Mickey Mouse y Goofy, y tiene una novia llamada Daisy Duck. Donald se mete en situaciones cómicas pero siempre demuestra lealtad y generosidad.'),
('Goofy', 'Goofy es un personaje optimista y torpe conocido por su risa contagiosa. A menudo se encuentra en situaciones ridículas debido a su naturaleza despistada. Es un amigo fiel de Mickey Mouse y Donald, y aunque sus torpezas causan problemas, siempre intenta ayudar a sus amigos.'),
('Minnie Mouse', 'Minnie Mouse es la novia de Mickey Mouse, conocida por su dulzura y su gran lazo. Es una figura solidaria y maternal que participa en aventuras con Mickey y la pandilla. Su personalidad amable y su amor por Mickey la convierten en una figura icónica de Disney.'),
('Pluto', 'Pluto es el perro mascota de Mickey Mouse, conocido por su lealtad y actitud juguetona. Aunque no habla, se expresa a través de ladridos y lenguaje corporal. Es un amigo cercano de la pandilla de Mickey y se encuentra en situaciones cómicas debido a su curiosidad.'),
('Daisy Duck', 'Daisy Duck es la novia del Pato Donald, conocida por su elegancia y carácter fuerte. Tiene una personalidad refinada pero también puede ser decidida y terca. Es amiga cercana de Minnie Mouse y participa en aventuras con ella y otros personajes de Disney.');


-- SELECCIONAR TODOS LOS DATOS DE LA TABLA DE PREGUNTAS
SELECT * FROM preguntas;
use personajes_test;


-- EJEMPLO DE CONSULTA CON JOIN (SI ES NECESARIO)
-- SELECT pj.ropa, preguntas.pregunta FROM pj, preguntas WHERE preguntas.id = 2 GROUP BY pj.ropa;
