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
    return 'Editar personaje'

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