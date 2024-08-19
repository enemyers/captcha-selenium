from flask import Flask
from modules.patente import get_placa
from modules.papeleta import get_papeleta

app = Flask(__name__)

# ROUTE
@app.route("/patente/<string:placa>")
def getplaca_route(placa):
    return get_placa(placa)

@app.route("/papeleta/<string:placa>")
def getpapeleta_route(placa):
    return get_papeleta(placa)

if __name__ == "__main__":
    app.run(debug=True, port=5300)