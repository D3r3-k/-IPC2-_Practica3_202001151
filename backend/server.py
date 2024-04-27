from flask import Flask, request
from flask_cors import CORS
from Objetos.Mascota import Perro, Gato, Conejo
import dicttoxml
import xmltodict

app = Flask(__name__)
CORS(app)

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
    try:
        mascotas_dict = xmltodict.parse(request.data)
        mascotas = mascotas_dict['ingresoAnimales']['perro']
        for mascota in mascotas:
            perro = Perro(mascota['raza'], mascota['edad'])
            perros.append(perro)
        mascotas = mascotas_dict['ingresoAnimales']['gato']
        for mascota in mascotas:
            gato = Gato(mascota['raza'], mascota['edad'])
            gatos.append(gato)
        mascotas = mascotas_dict['ingresoAnimales']['conejo']
        for mascota in mascotas:
            conejo = Conejo(mascota['raza'], mascota['edad'])
            conejos.append(conejo)
        dic_res = {
            "mensaje": "Se han registrado las mascotas correctamente"
        }
        return dicttoxml.dicttoxml(dic_res, custom_root='resultados', attr_type=False), 200
    except Exception as e:
        dic_res = {
            "mensaje": "Error al registrar mascotas"
        }
        return dicttoxml.dicttoxml(dic_res, custom_root='resultados', attr_type=False), 400


@app.route('/api/v1/mascotas', methods=['DELETE'])
def eliminar_mascota():
    perros.clear()
    gatos.clear()
    conejos.clear()
    # retornar un xml con un mensaje de confirmación
    dic_res = {
        "mensaje": "Se han eliminado todas las mascotas"
    }
    return dicttoxml.dicttoxml(dic_res, custom_root='resultados', attr_type=False), 200


if __name__ == '__main__':
    app.run(debug=True)
