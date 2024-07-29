from flask import Flask, flash, jsonify, redirect, request, render_template, url_for, session

import mysql.connector as connector
import os

app = Flask(__name__)
app.secret_key = 'mysecretkey'

p = '192.168.99.100'
def get_db_connection():
    db_config = {
        'host': ip,
        'user': 'root',
        'password': 'mi_contraseña',
        'database': 'personajes_test',
        'port': 3306
    }
    connection = connector.connect(**db_config)
    return connection

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/personajes')
def lista():
    page = int(request.args.get('page', 1))
    per_page = 1  # Mostrar una página a la vez
    offset = (page - 1) * per_page

    connection = get_db_connection()
    myCursor = connection.cursor()

    query = """
    SELECT pj.nombre, pj.edad, pj.pelo, pj.raza, pj.genero, pj.color, cuentos.nombre, cuentos.sinopsis
    FROM pj
    JOIN cuentos ON cuentos.id = pj.id
    LIMIT %s OFFSET %s;
    """
    myCursor.execute(query, (per_page, offset))
    results = myCursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in myCursor.description]

    # Convertir los resultados a una lista de diccionarios
    result_list = [dict(zip(column_names, row)) for row in results]

    # Obtener el total de personajes para calcular el número de páginas
    myCursor.execute("SELECT COUNT(*) FROM pj")
    total = myCursor.fetchone()[0]
    pages = (total + per_page - 1) // per_page

    myCursor.close()
    connection.close()

    return render_template('personajes.html', results=result_list, page=page, pages=pages)


@app.route('/editar')
def editar():
    connection = get_db_connection()
    myCursor = connection.cursor()
    query = "SELECT * FROM pj"
    myCursor.execute(query)
    result = myCursor.fetchall()
    
    myCursor.close()
    connection.close()
    return render_template('editar.html', results=result)

@app.route('/listo/<string:id>', methods=['POST','GET'])
def listo(id):
    connection = get_db_connection()
    myCursor = connection.cursor()
    query = "SELECT * FROM pj WHERE id=%s"
    myCursor.execute(query, (id,))
    result = myCursor.fetchall()
        
    myCursor.close()
    connection.close()
    return render_template('listo.html', results= result[0])

@app.route('/actualizar/<string:id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        ropa = request.form['ropa']
        pelo = request.form['pelo']
        raza = request.form['raza']
        genero = request.form['genero']
        color = request.form['color']

        connection = get_db_connection()
        myCursor = connection.cursor()
        query = """
            UPDATE pj SET nombre=%s, edad=%s, ropa=%s, pelo=%s, raza=%s, genero=%s, color=%s 
            WHERE id=%s
        """
        values = (nombre, edad, ropa, pelo, raza, genero, color, id)
        myCursor.execute(query, values)
        connection.commit()
        
        myCursor.close()
        connection.close()
        
        flash('Personaje actualizado', 'success')
        return redirect(url_for('editar'))

@app.route('/eliminar/<string:id>',methods=['POST'])
def eliminar(id):
    connection = get_db_connection()
    myCursor = connection.cursor()
    query = "DELETE FROM pj WHERE id = %s"
    myCursor.execute(query, (id,))
    connection.commit()

    myCursor.close()
    connection.close()

    flash('Personaje eliminado exitosamente')

    return redirect(url_for('editar'))

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        ropa = request.form['ropa']
        pelo = request.form['pelo']
        raza = request.form['raza']
        genero = request.form['genero']
        color = request.form['color']

        db = get_db_connection()
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO pj (nombre, edad, ropa, pelo, raza, genero, color) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (nombre, edad, ropa, pelo, raza, genero, color))
            db.commit()

            flash('personaje agregado correctamente')

        except connector.Error as err:
            print(f"Error: {err}")
            db.rollback()

        finally:
            cursor.close()
            db.close()

        return redirect(url_for('editar'))
    return render_template('agregar.html')

# Módulo Jugar
preguntas = [
    {"atributo": "edad", "pregunta": "¿En qué rango de edad se encuentra tu personaje?", "opciones": ["niño", "joven", "adulto"]},
    {"atributo": "pelo", "pregunta": "¿De qué color es el pelo de tu personaje?", "opciones": ["rubio", "negro", "rojo", "ninguno", "blanco"]},
    {"atributo": "raza", "pregunta": "¿Es humano tu personaje?", "opciones": ["Sí", "No"], "Sí": "humano", "No": "no humano"},
    {"atributo": "genero", "pregunta": "¿Tu personaje es mujer?", "opciones": ["Sí", "No"], "sí": "mujer", "no": "hombre"},
    {"atributo": "color", "pregunta": "¿Qué color representa a tu personaje?", "opciones": ["celeste", "rosa", "rojo", "azul", "amarillo", "marrón", "verde", "naranja", "violeta"]}
]
    # Convertir la respuesta en función de la pregunta específica
   
@app.route('/jugar')
def iniciar_juego():
    session.clear()
    session['pregunta_actual'] = 0
    session['candidatos'] = None
    return render_template('jugar.html', question=preguntas[0]["pregunta"], options=preguntas[0].get("opciones"))

@app.route('/rta', methods=['POST'])
def responder():
    respuesta = request.form['answer']
    pregunta_actual = session.get('pregunta_actual', 0)
    pregunta = preguntas[pregunta_actual]
    atributo = pregunta["atributo"]
    
    if atributo == "raza":
        # Mapea la respuesta a "humano" o "no humano"
        if respuesta in pregunta:
            valor_esperado = pregunta[respuesta]
        else:
            valor_esperado = respuesta

    elif atributo == "genero":
        # Mapea la respuesta a "mujer" o "hombre"
        respuesta_lower = respuesta.lower()
        if respuesta_lower in pregunta:
            valor_esperado = pregunta[respuesta_lower]
        else:
            valor_esperado = respuesta

    else:
        # Para otros atributos, simplemente usa la respuesta proporcionada
        valor_esperado = respuesta


    if session.get('candidatos') is None:
        conexion = get_db_connection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM pj")
        session['candidatos'] = cursor.fetchall()
        session['nombres_columnas'] = [desc[0] for desc in cursor.description]
        cursor.close()
        conexion.close()

    indices_columnas = {desc: index for index, desc in enumerate(session['nombres_columnas'])}
    indice_atributo = indices_columnas[atributo]
    
    print(f"Atributo actual: {atributo}")
    print(f"Valor esperado: {valor_esperado}")

    nuevos_candidatos = [
        personaje for personaje in session['candidatos']
        if personaje[indice_atributo] == valor_esperado
    ]

    session['candidatos'] = nuevos_candidatos

    print(f"Candidatos antes del filtrado: {session['candidatos']}")
    print(f"Candidatos después del filtrado: {nuevos_candidatos}")

    if len(nuevos_candidatos) == 1:
        result = nuevos_candidatos[0][session['nombres_columnas'].index('nombre')]
        return render_template('jugar.html', result=result)
    
    elif len(nuevos_candidatos) == 0 or pregunta_actual + 1 >= len(preguntas):
        return render_template('jugar.html', result="No se pudo determinar el personaje")
    
    else:
        session['pregunta_actual'] += 1
        siguiente_pregunta = preguntas[session['pregunta_actual']]["pregunta"]
        siguientes_opciones = preguntas[session['pregunta_actual']].get("opciones")
        return render_template('jugar.html', question=siguiente_pregunta, options=siguientes_opciones)
    

    #############################################################

@app.route('/personajes')
def pj():
        page = int(request.args.get('page', 1))
        per_page = 10
        offset = (page - 1) * per_page

        # Conectar a la base de datos
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute('SELECT COUNT(*) FROM cuentos')
        total = cursor.fetchone()[0]
        pages = (total + per_page - 1) // per_page

        cursor.execute('SELECT * FROM cuentos LIMIT %s OFFSET %s', (per_page, offset))
        results = cursor.fetchall()

        cursor.close()
        db.close()

        return render_template('personajes.html', results=results, previous_page=max(1, page - 1), next_page=min(pages, page + 1))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')



'''@app.route('/personajes', methods=['GET', 'POST'])
def pj():
    if request.method =='POST':
        id_char= request.form['id_pj']
        
        connection = get_db_connection()
        myCursor = connection.cursor()
        query = "SELECT nombre, edad, pelo, raza, genero, color FROM pj WHERE id = %s LIMIT 1;"
        
        myCursor.execute(query, (id_char,))
        result = myCursor.fetchall()

        myCursor.close()
        connection.close()

    return render_template('read.html', results=result)'''

    
'''def root():
    return "root" #Que es lo que devuelve
'''

'''
GET OBTENER DATOS
POST CREAR INFORMACION
PUT ACTUALIZAR INFORMACION
DELETE BORRAR INFORMACION

@app.route('/quest', methods=['POST'])
def create():
    data = request.get_json()
    return jsonify(data), 201
'''