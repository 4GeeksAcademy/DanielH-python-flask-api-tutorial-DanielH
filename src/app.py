from flask import Flask, jsonify
from flask import request


app = Flask(__name__)
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# danielh

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return  json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():    
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)





# @app.route('/todos/<int:position>', methods=['DELETE'])
# def delete_todo(position):
#     print("This is the position to delete: ", position)
#     if position < len(todos):
#         del todos[position]
#         return jsonify({"message": "Eliminacion correcta"})
#     else:
#         return jsonify({"error": "Posicion fuera de rango"}), 400


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)
    if 0 <= position < len(todos):
        del todos[position]
        return jsonify(todos)
    else:
        return jsonify({"error": "Invalid position"}), 400



# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)