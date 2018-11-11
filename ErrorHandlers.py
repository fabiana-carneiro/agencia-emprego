#################################################
# Servidor Web - Tratamento de Erros HTTP
#################################################

from Server import App
from Response import Response
from flask import jsonify

@App.errorhandler(500)
def TratarServerError(error):
    Response["Status"] = "Erro"
    Response["Mensagem"] = "Houve um erro interno no servidor, desculpe-nos pelo transtorno. Detalhe: {0}".format(error)
    Response["Dados"] = ""
    return(jsonify(Response))

@App.errorhandler(400)
def TratarClientError(error):
    Response["Status"] = "Erro"
    Response["Mensagem"] = "Houve um erro no seu pedido. Detalhe: {0}".format(error)
    Response["Dados"] = ""
    return(jsonify(Response))

@App.errorhandler(404)
def TratarNotFound(error):
    Response["Status"] = "Erro"
    Response["Mensagem"] = "Acao nao disponivel"
    Response["Dados"] = ""
    return(jsonify(Response))