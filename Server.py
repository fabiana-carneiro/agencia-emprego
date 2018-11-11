#################################################
# Servidor Web - REST API
#################################################

from flask import Flask
from flask import jsonify

App = Flask(__name__)

from Response import *
from ErrorHandlers import *
from Funcionarios.Routes import *
from Candidatos.Routes import *
from Enderecos.Routes import *
from Funcoes.Routes import *
from Clientes.Routes import *
from Vagas.Routes import *
from Entevistas.Routes import *
from Professores.Routes import *
from Cursos.Routes import *


if __name__ == "__main__":
    App.run(port=80, debug=False)