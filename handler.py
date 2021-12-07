import requests
import json

def temperatura(event, context):
    temp = requests.get("https://api.weatherapi.com/v1/current.json?key=25db6da1fd1f4fdbbb933615210712&q=Santiago&aqi=no")

    response = {"statusCode": 200, "body": json.dumps(temp.json().get("current").get("temp_c"))}

    return response

def UF(event, context):
    uf = requests.get("https://mindicador.cl/api")

    response = {"statusCode": 200, "body": json.dumps(uf.json().get("uf"))}

    return response

def dolar(event, context):
    dolar = requests.get("https://mindicador.cl/api")

    response = {"statusCode": 200, "body": json.dumps(dolar.json().get("dolar"))}

    return response

def crucigrama(event, context):

    response = {"statusCode": 200, "body": json.dumps({"url": "https://www.emol.com/servicios/juegos/crucigrama.aspx"})}

    return response

def apitoday(event, context):
    temp = requests.get("https://api.weatherapi.com/v1/current.json?key=25db6da1fd1f4fdbbb933615210712&q=Santiago&aqi=no")
    uf = requests.get("https://mindicador.cl/api")
    dolar = requests.get("https://mindicador.cl/api")
    crucigrama= "https://www.emol.com/servicios/juegos/crucigrama.aspx"

    response = {"statusCode": 200, "body": json.dumps({"temp": temp.json().get("current").get("temp_c"),
                                                        "uf": uf.json().get("uf"), 
                                                        "dolar": dolar.json().get("dolar"), 
                                                        "crucigrama": crucigrama})}

    return response