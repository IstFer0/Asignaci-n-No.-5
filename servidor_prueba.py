from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/nomina", methods=["POST"])
def recibir_nomina():
    datos = request.get_json()
    print(f"Datos recibidos: {datos}")
    return jsonify({"mensaje": "Datos recibidos correctamente"}), 201

if __name__ == "__main__":
    app.run(debug=True)