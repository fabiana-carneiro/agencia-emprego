#################################################
# Web API Cidades
# Mapeamento de Rotas
#################################################

from flask import jsonify, request
from Server import App, Response


@App.route("/cidades", methods=["GET"])
def ListarCidades():
    from Cidades.Services.ListarCidade import ListarCidades
    Dados = ListarCidades()
    Response["Dados"] = {"Cidades": Dados}
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)


@App.route("/cidades/<int:Id>", methods=["GET"])
def ConsultarPorId(Id):
    from Cidades.Services.ConsultarPorId import ConsultarPorId
    Dados = ConsultarPorId(Id)
    Response["Dados"] = Dados
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)


@App.route("/cidades", methods=["POST"])
def CadastrarCidades():
    from Cidades.Services.CadastrarCidade import CadastrarCidades

    Dados = request.get_json()
    Id = Dados["Id"]
    Nome = Dados["Nome"]
    Bairro = Dados["Bairro"]
    Uf = Dados["Uf"]
    CadastrarCidades(Id, Nome, Bairro, Uf)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)


@App.route("/cidades", methods=["PUT"])
def AtualizarCidades():
    from Cidades.Services.AtualizarCidade import AtualizarCidade

    Dados = request.get_json()
    Id = Dados["Id"]
    Nome = Dados["Nome"]
    Bairro = Dados["Bairro"]
    Uf = Dados["Uf"]
    Ativo = Dados["Ativo"]
    AtualizarCidade(Id, Nome, Bairro, Uf, Ativo)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)


@App.route("/cidades/<int:Id>", methods=["DELETE"])
def InativarCidade(Id):
    from Cidades.Services.InativarCidade import InativarCidade
    InativarCidade(Id)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)