from flask import Flask, request, jsonify
from datetime import datetime
import uuid
from dotenv import load_dotenv
load_dotenv()
import os
app = Flask(__name__)

BASE_URL = os.environ.get('API_BASE_URL', 'http://localhost')
PORT = os.environ.get('API_PORT', 6003)

@app.route('/api/negocio/v10/status', methods=['GET'])
def get_status():
    return jsonify({
        "status": "OK",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0",
        "service": "API - Ingreso Pedido Lista"
    }), 200

@app.route("/api/negocio/v10/insert-pedidos", methods=["POST"])

@app.route("/api/negocio/v10/insert-pedidos-list", methods=["POST"])
def insert_pedidos_list():
    pedidos = request.json
    
    if not isinstance(pedidos, list):
        pedidos = [pedidos]
    
    process_id  =str(uuid.uuid4())
    process_count = 0
    error_count = 0
    errores = []

    for pedido in pedidos:
        required_fields = ['numCliente', 'codProducto', 'codTipoSolicitud', 'importe', 'esTotal', 'idFormaPago', 'idPedido', 'requiereAutorizacion']
       
        missing_fields = [field for field in required_fields if field not in pedido]
        if missing_fields:
            error_count += 1
            errores.append(f"Faltan los campos: {', '.join(missing_fields)} en el pedido: {pedido.get('idPedido', 'sin ID')}")
            continue
        process_count += 1
        
    response = {
            "idProceso": process_id,
            "cantidadErrores": error_count,
            "cantidadOperacionesProcesadas": process_count,
            "errores": errores
        }
        
    return jsonify(response), 200 if error_count == 0 else 400
    
if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port=PORT)
    
print(f"API running on {BASE_URL}:{PORT}")