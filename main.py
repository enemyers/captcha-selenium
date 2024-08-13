from flask import Flask
from modules.captcha import get_placa

app = Flask(__name__)

# ROUTE
@app.route("/placa/<string:placa>")
def getplaca_route(placa):
    return get_placa(placa)

if __name__ == "__main__":
    app.run(debug=True, port=5300)