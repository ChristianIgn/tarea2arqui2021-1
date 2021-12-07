import requests
import json

# res = requests.get('https://reqres.in/api/users?page=2')
# print(f'Total users: {res.json().get("total")}')
def UF(event, context):
    uf = requests.get("https://mindicador.cl/api")

    response = {"statusCode": 200, "body": str(uf.json().get("uf"))}

    return response

def dolar(event, context):
    dolar = requests.get("https://mindicador.cl/api")

    response = {"statusCode": 200, "body": str(dolar.json().get("dolar"))}

    return response
