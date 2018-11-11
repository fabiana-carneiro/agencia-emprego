#################################################
# Web API Funções
# Mapeamento de Rotas
#################################################

from flask import jsonify, request
from Server import App, Response

@App.route("/funcoes", methods=["GET"])
def ListarFuncoes():
    from Funcoes.Services.ListarFuncoes import ListarFuncoes
    Dados = ListarFuncoes()
    Response["Dados"] = {"Funcoes":Dados}
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/funcoes/<int:Id>", methods=["GET"])
def ConsultarPorId(Id):
    from Funcoes.Services.ConsultarPorId import ConsultarPorId
    Dados = ConsultarPorId(Id)
    Response["Dados"] = Dados
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/funcoes", methods=["POST"])
def CadastrarFuncao():
    from Funcoes.Services.CadastrarFuncao import CadastrarFuncao
    
    Dados = request.get_json()
    Id = Dados["Id"]
    Nome = Dados["Nome"]
    Nivel = Dados["Nivel"]
    CadastrarFuncao(Id, Nome, Nivel)
    
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/funcoes", methods=["PUT"])
def AtualizarFuncao():
    from Funcoes.Services.AtualizarFuncao import AtualizarFuncao
    
    Dados = request.get_json()
    Id = Dados["Id"]
    Nome = Dados["Nome"]
    Nivel = Dados["Nivel"]
    Ativo = Dados["Ativo"]
    AtualizarFuncao(Id, Nome, Nivel, Ativo)
    
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/funcoes/<int:Id>", methods=["DELETE"])
def InativarFuncao(Id):
    from Funcoes.Services.InativarFuncao import InativarFuncao
    InativarFuncao(Id)
    
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)