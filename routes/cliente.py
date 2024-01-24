from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)


@cliente_route.route('/')
def lista_clientes():
  """-- /clientes/ (GET) - lista os clientes"""
  return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
  """-- /clientes/ (POST) - inserir o cliente no servidor"""
  data = request.json
  
  novo_usuario = {
    "id": len(CLIENTES) + 1, 
    "nome": data['nome'],
    "email": data['email']
  }
  CLIENTES.append(novo_usuario)
  
  return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def form_cliente():
  """-- /clientes/new (GET) - renderiza um formulario para criar um cliente"""
  return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
  """-- /clientes/<id> (GET) - obter os dados de um cliente"""
  
  cliente = list(filter(lambda c: c['id'] == cliente_id, CLIENTES))[0]
  return render_template('detalhe_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
  """-- /clientes/<id>/edit (GET) - renderizar um formulario para editar o cliente"""
  cliente = None
  for c in CLIENTES:
    if c['id'] == cliente_id:
      cliente = c
  
  return render_template('form_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
  """-- /clientes/<id>/update (PUT) - renderizar um formulario para editar o cliente"""
  cliente_editado = None
  
  data = request.json
  
  for c in CLIENTES:
    if c['id'] == cliente_id:
      c['nome'] = data['nome']
      c['email'] = data['email']
      
      cliente_editado = c
  return render_template('item_cliente.html', cliente=cliente_editado)

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_cliente(cliente_id):
  """-- /clientes/<id/delete (DELETE) - deleta o registro do usuario"""
  global CLIENTES
  CLIENTES = [c for c in CLIENTES if c['id'] != cliente_id]
  
  return {"delete": "ok"}

