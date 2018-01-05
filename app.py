from flask import Flask, render_template, json, request, jsonify
from PIL import Image
import os
from request_DL import *
from mongo_DL import *
from Mails_DL import *
import datetime

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/many', methods=['POST'] )
def test3():
    task = get_form_found(request.form)
    print insert_dog_lost(task)

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
      img.save(pwd)
      n=n+1
    return "OK", 201

@app.route('/upload_image', methods=['POST'])
def image():
    img = Image.open(request.files['inputFile'])
    img.show()
    img.save("./cnn/final.jpg")
    os.system('bash ./cnn/run_cnn.sh')
    data  = get_results_classify()
    array = tasks
    get_dates_user(data, array)
    return "OK", 201

if __name__ == "__main__":
    app.run(port=5000)
