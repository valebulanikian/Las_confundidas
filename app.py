from flask import Flask, flash, jsonify, redirect, request, render_template, url_for
import mysql.connector as connector
import os

app = Flask(__name__)
app.secret_key = 'mysecretkey'


@app.route('/')
def home():
    return render_template('index.html')

def get_db_connection():
    db_config = {
        'host': 'db',
        'user': 'mysql',
        'password': 1234,
        'database': 'personajes_test',
        'port': 3306
    }
    connection = connector.connect(
                user='mysql', 
                password=1234,
                host='db', # name of the mysql service as set in the docker compose file
                database='personajes_test',
                auth_plugin='mysql_native_password')

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
        
        flash('Contacto actualizado', 'success')
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

    flash('Contacto eliminado exitosamente')

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