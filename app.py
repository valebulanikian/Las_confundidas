from flask import Flask, jsonify, request, render_template # type: ignore
import mysql.connector

app=Flask(__name__)

@app.route('/') #Decorador, endpoint

def home():
    return render_template('index.html')

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="personajes_test"

    )
    return connection

@app.route('/personajes')
def lista():
    connection = get_db_connection()
    myCursor = connection.cursor()
    query = "SELECT nombre, edad, pelo, raza, genero, color FROM pj"
    myCursor.execute(query)
    result = myCursor.fetchall()
    
    myCursor.close()
    connection.close()

    return render_template('personajes.html', results=result)

@app.route('/editar')
def editar():
    connection = get_db_connection()
    myCursor = connection.cursor()
    query = "SELECT id, nombre, edad, pelo, raza, genero, color FROM pj"
    myCursor.execute(query)
    result = myCursor.fetchall()
    myCursor.close()
    connection.close()

    return render_template('editar.html', results=result)

@app.route('/listo', methods=['GET', 'POST'])
def listo():
    if request.method == 'POST':
        id = request.form.get('id') 
        nombre = request.form.get('nombre')
        edad = request.form.get('edad')
        pelo = request.form.get('pelo')
        raza = request.form.get('raza')
        genero = request.form.get('genero')
        color = request.form.get('color')
        
        if not id:
            mensajes="ID no proporcionado."
            return mensajes
        
        try:
            connection = get_db_connection()
            myCursor = connection.cursor()
            query = """
                UPDATE pj 
                SET nombre = %s, edad = %s, pelo = %s, raza = %s, genero = %s, color = %s
                WHERE id = %s
            """
            valores = (nombre, edad, pelo, raza, genero, color, id)
            myCursor.execute(query, valores)
            connection.commit()
            myCursor.close()
            connection.close()
            mensaje = "Registro actualizado exitosamente."
        except Exception as e:
            mensaje = f"Error al actualizar el registro: {e}"

        return render_template('listo.html', mensaje=mensaje)
    return render_template('listo.html')

@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    if request.method == "POST":
        id=request.form.get('id')

    if not id:
            mensajes="ID no proporcionado."
            return mensajes
    
    try:
            connection = get_db_connection()
            myCursor = connection.cursor()
            query = """
                DELETE FROM pj
                WHERE id = %s
            """
            myCursor.execute(query, (id,))
            connection.commit()
            myCursor.close()
            connection.close()
            mensaje = "Registro eliminado"
    except Exception as e:
            mensaje = f"Error al eliminar el registro: {e}"

    return render_template('editar.html', mensaje=mensaje)


@app.route('/agregar')
def agregar():
    return 'Agregar personaje'

if __name__=="__main__":
    app.run(debug=True)








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