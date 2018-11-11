#################################################
# Web API Cursos
# Mapeamento de Rotas
#################################################

from flask import jsonify, request
from Server import App, Response


@App.route("/cursos", methods=["GET"])
def ListarCursos():
    from Cursos.Services.ListarCurso import ListarCurso
    Dados = ListarCurso()
    Response["Dados"] = {"Cursos": Dados}
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)


@App.route("/cursos/<int:Id>", methods=["GET"])
def ConsultarPorId(Id):
    from Cursos.Services.ConsultarPorId import ConsultarPorId
    Dados = ConsultarPorId(Id)
    Response["Dados"] = Dados
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)


@App.route("/cursos", methods=["POST"])
def CadastrarCurso():
    from Cursos.Services.CadastrarCurso import CadastrarCurso

    Dados = request.get_json()
    Id = Dados["Id"]
    Nome = Dados["Nome"]
    Duracao = Dados["Duracao"]
    CodProfessor = Dados["CodProfessor"]
    CadastrarCurso(Id, Nome, Duracao, CodProfessor)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)


@App.route("/cursos", methods=["PUT"])
def AtualizarCurso():
    from Cursos.Services.AtualizarCurso import AtualizarCurso

    Dados = request.get_json()
    Id = Dados["Id"]
    Nome = Dados["Nome"]
    Duracao = int(Dados["Duracao"])
    CodProfessor = int(Dados["CodProfessor"])
    Ativo = Dados["Ativo"]
    AtualizarCurso(Id, Nome, Duracao, CodProfessor, Ativo)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)


@App.route("/cursos/<int:Id>", methods=["DELETE"])
def InativarCurso(Id):
    from Cursos.Services.InativarCurso import InativarCurso
    InativarCurso(Id)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)