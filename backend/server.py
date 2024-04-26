from flask import Flask, request
from Objetos.Mascota import Perro, Gato, Conejo
import dicttoxml
import re
import xmltodict

app = Flask(__name__)

perros = []
gatos = []
conejos = []


@app.route('/api/v1/mascotas', methods=['GET'])
def mostrar_registro():
    dic_res = {
        "animales": {
            "perros": {
                "cantidadTotal": len(perros),
            },
            "gatos": {
                "cantidadTotal": len(gatos),
            },
            "conejos": {
                "cantidadTotal": len(conejos),
            }
        }
    }
    return dicttoxml.dicttoxml(dic_res, custom_root='resultados', attr_type=False), 200


@app.route('/api/v1/mascotas', methods=['POST'])
def registrar_mascota():
    mascotas_dict = xmltodict.parse(request.data)
    for key, value in mascotas_dict['ingresoAnimales'].items():
        if key == 'perro':
            perro = Perro(value['edad'], value['raza'])
            perros.append(perro)
        elif key == 'gato':
            gato = Gato(value['edad'], value['raza'])
            gatos.append(gato)
        elif key == 'conejo':
            conejo = Conejo(value['edad'], value['raza'])
            conejos.append(conejo)
    return 'Mascotas registradas', 201


@app.route('/api/v1/mascotas', methods=['DELETE'])
def eliminar_mascota():
    perros.clear()
    gatos.clear()
    conejos.clear()
    return 'Mascotas eliminadas', 200


if __name__ == '__main__':
    app.run(debug=True)
