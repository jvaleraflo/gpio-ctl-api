# HTTP Method URI Action
# ===============================================================================
# GET         http://0.0.0.0/GPIOs/       Devuelve el estado de todos los gpios
# GET         http://0.0.0.0/GPIOs/[gpio] Devuelve el estado de un gpio
# POST        http://0.0.0.0/GPIOs/[gpio] Inicia la gestion de un gpio
# DELETE      http://0.0.0.0/GPIOs/[gpio] Retira la gestion de un gpio

# PUT         http://0.0.0.0/GPIOs/[gpio]/[value] Modifica las caracteristicas de un gpio
# ===============================================================================


from flask import Flask, request
from flask_restful import Resource, Api

import RPi.GPIO as GPIO

app = Flask(__name__)
api = Api(app)

# Establezco modo BCM para referenciar los gpios
GPIO.setmode(GPIO.BCM)

# Diccionario con los gpios almacenando sus caracteristicas
# key. numero de GPIO
# values. uso: dir: value
# 17 : {'uso' : 'relay enchufe 1', 'dir' : 'out', 'value' : 'low'}
gpios = {}



class Gpios_List_API(Resource):
    def get(self, todo_id):
        return {gpios}


class Gpio_Do_API(Resource):
    def get(self, gpio):
        return {gpios.get(gpio)}

    def POST(self, gpio):
        gpios.update(gpio)
        return {'insertado ' + gpio}
    
    def delete(self, gpio):
        gpios.pop(gpio)
        return {'borrado ' + gpio}


api.add_resource(Gpios_List_API, '/GPIOs')
api.add_resource(Gpio_Do_API,'/GPIOs/<int:gpio>')


if __name__ == '__main__':
    app.run(debug=False, port=2008, host='0.0.0.0')