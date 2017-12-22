import json
import ast
#Armar json
def get_form_found(request):
  json = {
          'id': 1,
          'Fecha': request['inputFecha'],
          'Talla': request['inputTalla'],
          'Lugar': request['inputLugar'],
          'Color': request['inputColor'],
          'Sexo': request['inputSexo'],
          'Name': request['inputDogName'],
          'data_user':{
                       'Name': request['inputName'],
                       'Email': request['inputEmail']
                      }
         }
  return json

def get_results_classify():
  file_results = open("./cnn/results_classify.txt", "r") 
  contenido = file_results.read()
  array = ast.literal_eval(contenido)
  return array[0]

def get_dates_user(data, array):
  for key  in array:
    print data
    print key['data_user']['Email']
  
