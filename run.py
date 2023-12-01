from flask import Flask, redirect
from app.routes.usuarios import usuarios

server = Flask(__name__)
server.register_blueprint(usuarios, url_prefix='/usuarios')

@server.route('/')
def redireccionarToUsuarios():
    return redirect('/usuarios/obtener')

if __name__ == '__main__':
    server.run(debug=True, port=3000)
