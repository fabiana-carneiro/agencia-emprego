#################################################
# Web API Professores
# Mapeamento de Rotas
#################################################

from flask import jsonify, request
from Server import App, Response


@App.route("/professores", methods=["GET"])
def ListarProfessores():
    from Professores.Services.ListarProfessor import ListarProfessor
    Dados = ListarProfessor()

    Response["Dados"] = {"Professores": Dados}
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)


@App.route("/professores/<int:Id>", methods=["GET"])
def ConsultarPorId(Id):
    from Professores.Services.ConsultarPorId import ConsultarPorId
    Dados = ConsultarPorId(Id)

    Response["Dados"] = Dados
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)


@App.route("/professores", methods=["POST"])
def CadastrarProfessor():
    from Professores.Services.CadastrarProfessor import CadastrarProfessor

    Dados = request.get_json()
    Id = Dados["Id"]
    Nome = Dados["Nome"]
    Idade = Dados["Idade"]
    Cpf = Dados["Cpf"]
    CadastrarProfessor(Id, Nome, Idade, Cpf)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)


@App.route("/professores", methods=["PUT"])
def AtualizarProfessor():
    from Professores.Services.AtualizarProfessor import AtualizarProfessor

    Dados = request.get_json()
    Id = Dados["Id"]
    Nome = Dados["Nome"]
    Idade = Dados["Idade"]
    Cpf = Dados["Cpf"]
    Ativo = Dados["Ativo"]
    AtualizarProfessor(Id, Nome, Idade, Cpf, Ativo)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)


@App.route("/professores/<int:Id>", methods=["DELETE"])
def InativarProfessore(Id):
    from Professores.Services.InativarProfessor import InativarProfessor
    InativarProfessor(Id)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)