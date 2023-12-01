from flask import Blueprint, jsonify
from app.controllers.usuariosController import UsuariosController

usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/obtener')
def obtener_usuario():
    return  UsuariosController.obtenerUsuarios()

@usuarios.route('/minimo')
def obtener_minimo():
    return  UsuariosController.obtenerUsuarioMinimo()