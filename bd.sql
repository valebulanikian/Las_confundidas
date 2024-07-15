use personajes_test;

create table preguntas(
	id int auto_increment primary key,
    pregunta varchar(200)
);

insert into preguntas (pregunta)
values ('¿En qué rango de edad se encuentra tu personaje?'), 
		('¿Qué tipo de ropa usa?'), 
        ('¿Es de raza humana?'),
        ('¿Es una mujer?'),
        ('¿Qué color representa mejor a tu personaje?');

select * from preguntas;


select ropa, pregunta from pj, preguntas
where preguntas.id=2
group by ropa;

