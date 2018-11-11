#################################################
# Web API Vagas
# Mapeamento de Rotas
#################################################

from Server import App, Response
from flask import request, jsonify

@App.route("/vagas", methods=["GET"])
def ListarVagas():
    from Vagas.Services.ListarVagas import ListarVagas
    Dados = ListarVagas()
    Response["Dados"] = {"Vagas":Dados}
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/vagas/<int:Id>", methods=["GET"])
def ConsultarPorId(Id):
    from Vagas.Services.ConsultarPorId import ConsultarPorId
    Dados = ConsultarPorId(Id)
    Response["Dados"] = Dados
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/vagas", methods=["POST"])
def CadastrarVaga():
    from Vagas.Services.CadastrarVaga import CadastrarVaga

    Dados = request.get_jason()
    Id = Dados["Id"]
    Descricao = Dados["Descricao"]
    Salario = Dados["Salario"]
    Escolaridade=  Dados["Escolaridade"]
    CodCliente = Dados["CodCliente"]
    CodFuncao = Dados["CodFuncao"]
    CadastrarVaga(Id, Descricao, Salario, Escolaridade, CodCliente, CodFuncao)

    Response["Dados"] = Dados
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/vagas", methods=["PUT"])
def AtualizarVaga():
    from Vagas.Services.AtualizarVaga import AtualizarVaga

    Dados = request.get_jason()
    Id = Dados["Id"]
    Descricao = Dados["Descricao"]
    Salario = Dados["Salario"]
    Escolaridade = Dados["Escolaridade"]
    CodCliente = Dados["CodCliente"]
    CodFuncao = Dados["CodFuncao"]
    Ativo = Dados["Ativo"]
    AtualizarVaga(Id, Descricao, Salario, Escolaridade, CodCliente, CodFuncao, Ativo)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/vagas/<int:Id>", methods=["DELETE"])
def InativarVaga(Id):
    from Vagas.Services.InativarVaga import InativarVaga
    InativarVaga(Id)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)
