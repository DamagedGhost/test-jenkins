from flask import Flask
from prometheus_client import make_wsgi_app, Counter
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# Creamos la métrica que nos pide la pauta para Prometheus y Grafana
REQUESTS = Counter('http_requests_total', 'Total de peticiones HTTP')

# Configuramos la ruta /metrics para que Prometheus pueda raspar los datos
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

## @brief Inicia el servidor de la aplicación.
#  @details Esta función arranca Flask y registra una visita en la métrica.
@app.route('/')
def hello():
    REQUESTS.inc() # Incrementa la métrica cada vez que entras a la raíz
    return "App Segura funcionando perfectamente!"

if __name__ == '__main__':
    # host='0.0.0.0' es OBLIGATORIO en Docker para aceptar conexiones externas
    app.run(host='0.0.0.0', port=5000)