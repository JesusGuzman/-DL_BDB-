
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
  print json
