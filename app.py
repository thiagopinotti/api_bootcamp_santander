from playhouse.shortcuts import dict_to_model, model_to_dict
from flask import Flask, request, jsonify, json
from model import Cliente, Encomenda
# import jsonpickle

app = Flask(__name__)
app.json.sort_keys = False # desabilita a ordenação alfabetica no json 

@app.route('/clientes', methods=['GET'])
def get_clientes():
    if request.method == 'GET':
        cliente = Cliente.select().execute()
        # return jsonpickle.encode(list(map(model_to_dict, cliente)), unpicklable=False) # Estudar
        return jsonify(list(map(model_to_dict, cliente)))

@app.route('/clientes', methods=['POST'])
def set_clientes():
    if request.method == 'POST':
        cliente = dict_to_model(Cliente, request.get_json())
        cliente.save()
        return request.get_json()

@app.route('/clientes/<id>', methods=['GET'])
def get_cliente(id):
    if request.method == 'GET':
        cliente = Cliente.select().where(Cliente.id == id).get()
        # return jsonpickle.encode(model_to_dict(cliente), unpicklable=False) # Estudar
        return jsonify(model_to_dict(cliente))
    
@app.route('/clientes/<id>', methods=['PUT'])
def update_cliente(id):
    if request.method == 'PUT':
        dados = request.get_json()
        cliente = Cliente.get_by_id(id)
        cliente.nome = dados['nome']
        cliente.endereço = dados['endereço']
        cliente.save()
        # return jsonpickle.encode(model_to_dict(cliente), unpicklable=False) # Estudar
        return jsonify(model_to_dict(cliente))
    
@app.route('/clientes/<id>', methods=['DELETE'])
def delete_cliente(id):  
    if request.method == 'DELETE':
        Cliente.delete_by_id(id)
        return {'mensagem': 'Deletado'}
    
@app.route('/encomendas', methods=['GET'])
def get_encomendas():
    if request.method == 'GET':
        encomendas = Encomenda.select().execute()
        # return jsonpickle.encode(list(map(model_to_dict, encomendas)), unpicklable=False) # Estudar
        return jsonify(list(map(model_to_dict, encomendas)))


@app.route('/encomenda', methods=['POST'])
def add_encomenda():
    if request.method == 'POST':
        encomenda = dict_to_model(Encomenda, request.get_json())
        encomenda.save()
        return request.get_json()
    
app.run()
