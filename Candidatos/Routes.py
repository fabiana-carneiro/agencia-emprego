#################################################
# Web API Candidatos
# Mapeamento de Rotas
#################################################

from flask import jsonify, request
from Server import App, Response

@App.route("/candidatos", methods=["GET"])
def ListarCandidatos():
    from Candidatos.Services.ListarCandidato import ListarCandidatos
    Dados = ListarCandidatos()
    Response["Dados"] = {"Candidatos":Dados}
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/candidatos/<int:Id>", methods=["GET"])
def ConsultarPorId(Id):
    from Candidatos.Services.ConsultarPorId import ConsultarPorId
    Dados = ConsultarPorId(Id)
    Response["Dados"] = Dados
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/candidatos", methods=["POST"])
def CadastrarCandidato():
    from Candidatos.Services.CadastrarCandidato import CadastrarCandidato
    
    Dados = request.get_json()
    Id = Dados["Id"]
    Nome = Dados["Nome"]
    Cpf = Dados["Cpf"]
    Escolaridade = Dados["Escolaridade"]
    Telefone = Dados["Telefone"]
    Email = ["Email"]
    CadastrarCandidato(Id, Nome, Cpf, Escolaridade, Telefone, Email)
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/candidatos", methods=["PUT"])
def AtualizarCandidato():
    from Candidatos.Services.AtualizarCandidato import AtualizarCandidato
    
    Dados = request.get_json()
    Id = Dados["Id"]
    Nome = Dados["Nome"]
    Cpf = Dados["Cpf"]
    Escolaridade = Dados["Escolaridade"]
    Telefone = Dados["Telefone"]
    Email = ["Email"]
    Ativo = Dados["Ativo"]
    AtualizarCandidato(Id, Nome, Cpf, Escolaridade, Telefone, Email, Ativo)
    
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/candidatos/<int:Id>", methods=["DELETE"])
def InativarCandidato(Id):
    from Candidatos.Services.InativarCandidato import InativarCandidato    
    InativarCandidato(Id)
    
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)