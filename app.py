//este es el intermediario entre el html y el script cabe aclarar que algunas funciones no han sido modificadas
from flask import Flask, jsonify
from flask_cors import CORS

# Importa la función que quieres ejecutar desde tu otro archivo
# Suponiendo que en 'mi_script.py' tienes una función llamada 'hacer_algo()'
from mi_script import hacer_algo 

# --- Configuración del Servidor ---
app = Flask(__name__)
CORS(app)  # Esto permite que tu web se comunique con este servidor

# --- Definir la Ruta (Endpoint) ---
# Esta es la URL que tu JavaScript llamará.
# Cuando alguien visite '/ejecutar-script', se correrá la función de abajo.
@app.route("/ejecutar-script")
def ejecutar_mi_script():
    try:
        # 1. Llama a la función de tu script
        resultado = hacer_algo() 
        
        # 2. Prepara una respuesta para enviar de vuelta a la página web
        respuesta = {"status": "exitoso", "mensaje": resultado}
        return jsonify(respuesta)

    except Exception as e:
        # Si algo sale mal, envía un mensaje de error
        respuesta_error = {"status": "error", "mensaje": str(e)}
        return jsonify(respuesta_error), 500

# --- Iniciar el Servidor ---
# Esto hace que el servidor se ejecute cuando corras 'python app.py'
if __name__ == "__main__":
    app.run(debug=True, port=5000)
