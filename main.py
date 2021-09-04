import requests
import json
import sys
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class getData(Resource):
    def get(self):
        return {'about': 'Get-Data!'}

    def post(self):
        data_json = request.get_json()
        return {'Data': data_json}, 201

class Test(Resource):
    def get(self, datos):
        valor = ProcessData.scrappingWeb('https://www3.interrapidisimo.com/ApiRecogidas/api/Recogidas/GuiasPorRecogida?idRecogida=3070895')
        return {'result': valor}

class GetGuia(Resource):
    def get(self, guia):
        url = "https://www3.interrapidisimo.com/ApiservInter/api/Mensajeria/ObtenerRastreoGuias?guias="+guia
        page = requests.get(url)
        data = page.content.decode('utf-8')
        jsondata = json.loads(data)
        jsonrequest = {"Guia": jsondata[0]["TrazaGuia"]["NumeroGuia"],
                    "FechaAdmisionGuia": jsondata[0]["TrazaGuia"]["FechaAdmisionGuia"],
                    "FechaEstimadaEntrega": jsondata[0]["Guia"]["FechaEstimadaEntrega"],
                    "IdServicio": jsondata[0]["Guia"]["IdServicio"],
                    "NombreCiudadDestino": jsondata[0]["Guia"]["NombreCiudadDestino"],
                    "Destinatario": jsondata[0]["Guia"]["Destinatario"]["Nombre"],
                    "Direccion": jsondata[0]["Guia"]["Destinatario"]["Direccion"],
                       "EsAlcobro": jsondata[0]["Guia"]["EsAlCobro"],
                       "CreadoPor": jsondata[0]["Guia"]["CreadoPor"]}
        return jsonrequest

    def post(self, guia):
        url = "https://www3.interrapidisimo.com/ApiservInter/api/Mensajeria/ObtenerRastreoGuias?guias="+guia
        page = requests.get(url)
        data = page.content.decode('utf-8')
        jsondata = json.loads(data)
        jsonrequest = {"Guia": jsondata[0]["TrazaGuia"]["NumeroGuia"],
                       "FechaAdmisionGuia": jsondata[0]["TrazaGuia"]["FechaAdmisionGuia"],
                       "FechaEstimadaEntrega": jsondata[0]["Guia"]["FechaEstimadaEntrega"],
                       "IdServicio": jsondata[0]["Guia"]["IdServicio"],
                       "NombreCiudadDestino": jsondata[0]["Guia"]["NombreCiudadDestino"],
                       "Destinatario": jsondata[0]["Guia"]["Destinatario"]["Nombre"],
                       "Direccion": jsondata[0]["Guia"]["Destinatario"]["Direccion"],
                       "EsAlcobro": jsondata[0]["Guia"]["EsAlCobro"],
                       "CreadoPor": jsondata[0]["Guia"]["CreadoPor"]}
        return jsonrequest



api.add_resource(getData, '/')
api.add_resource(Test, '/test/<string:datos>')
api.add_resource(GetGuia, '/getguia/<string:guia>')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
