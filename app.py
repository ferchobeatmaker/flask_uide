import json
import requests
from flask import Flask, Response
from productos import Producto

app = Flask(__name__)


@app.route("/")
def hello_word():
    a="Master en Ciberseguridad-"
    b="UIDE"
    e= " JUAN FERNANDO GUACHAMIN "
    c = "-----Después del URL poner un slash y el criterio de búsqueda, ejemplo: PS4"
    d="-----https://uideflask.herokuapp.com/auto"
    return (a+b+e+c+d)

@app.route("/<producto>")
def buscar_Producto_en_wallapop(producto):
    wallapopoKeyWord = producto
    wallapopUrl = f"https://api.wallapop.com/api/v3/general/search?keywords={wallapopoKeyWord}%20&category_ids=12900&filters_source=seo_landing&longitude=-3.69196&latitude=40.41956&order_by=closest"
    r = requests.get(wallapopUrl)
    objetos_return_api = r.json().get("search_objects")
    #    objetos_return_api = r.json()
    lista_productos = []
    for p in objetos_return_api:
        lista_productos.append(Producto(titulo=p["title"], valor=p["price"], moneda=p["currency"]))

    lista_productos_dict = [t.to_dict() for t in lista_productos]
    lista_productos_serializada = json.dumps(lista_productos_dict)
    return Response(lista_productos_serializada)


if __name__ == "__main__":
    app.run()
