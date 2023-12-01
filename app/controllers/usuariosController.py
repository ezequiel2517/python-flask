import json, os
from flask import jsonify
from app.models.usuario import Usuario

class UsuariosController:        
    @classmethod
    def getUsuarioFromData(cls, file_name):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        filePath = os.path.join(os.pardir, "data", file_name)
        if os.path.exists(filePath):
            with open(filePath, 'r') as jsonFile:
                usuarioJson = json.load(jsonFile)
                return usuarioJson
        else:
            return None
    
    @staticmethod
    def obtenerUsuarios():
        usuarios = []
        for iter in range(1, 11):
            usuario = UsuariosController.getUsuarioFromData(f"u{str(iter).zfill(2)}.json")
            usuarios.append(usuario)
        return usuarios
    
    @staticmethod
    def obtenerUsuarioMinimo():
        data = UsuariosController.obtenerUsuarios()
        usuarios = [Usuario(user["user_id"], user["users_following"]) for user in data]
        minimo = min(usuarios, key=lambda user: user.countSeguidores())
        return {
            "user_id": minimo.user_id,
            "amount_of_followers": minimo.countSeguidores()
        }
