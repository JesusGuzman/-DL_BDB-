from flask import Flask, render_template, json, request, jsonify
from PIL import Image
import os
from request_DL import *
import datetime

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/signUp', methods=['POST'] )
def test():
    
    var = request.form['inputFecha']
    imgs = request.files['inputFile']
    img = Image.open(imgs)
    img.show()
    print var
    return jsonify({'task': tasks}), 201
 

@app.route('/many', methods=['POST'] )
def test3():
    task = get_form_found(request.form)
    print len(tasks)
    tasks.append(task)
    print len(tasks)
    imgs = request.files
    name_dog = request.form['inputDogName']
    email = request.form['inputEmail']
    date_now = datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    name_folder = name_dog +"_"+ email+"_"+date_now+"/"
    data = dict(imgs)
    datas = data['file[]']
     
    create_folder = "mkdir ./cnn/training_dataset/"+name_folder
    os.system(create_folder)
    
    n = 1
    for key in datas:
      pwd = "./cnn/training_dataset/"+name_folder+"perro"+str(n)+".jpg"
      img = Image.open(key)
      #img.save("./cnn/training_dataset/final.jpg")
      img.save(pwd)
      n=n+1
    return "hola", 201

@app.route('/dogs', methods=['GET'])
def get_dogs():
    return jsonify({'tasks': tasks})

@app.route('/new_dog', methods=['POST'])
def add_dog():
    var = request.json['nombre']
    task = {
        #'id': tasks[-1]['id'] + 1,
        #'nombre': request.json['nombre'],
        #'raza': request.json['raza'],
        #'edad': request.json['edad'],
        #'color': request.json['color'],
        #'descripcion': request.json['descripcion'],
        #'fecha de extravio': request.json['fecha'],
        #'lugar de extravio': request.json['lugar']
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/upload_image', methods=['POST'])
def image():
    img = Image.open(request.files['inputFile'])
    img.show()
    img.save("./cnn/final.jpg")
    os.system('bash ./cnn/run_cnn.sh')
    data = date_json = get_results_classify()
    array = tasks
    get_dates_user(data, array)
    return "OK"

tasks = [

]

if __name__ == "__main__":
    app.run(port=5000)
