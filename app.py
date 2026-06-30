from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    """
    @brief Devuelve un saludo personalizado.

    @param name Nombre del usuario recibido desde la query string.
    @return Mensaje de saludo en formato de texto.
    """

    name = request.args.get('name')
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)