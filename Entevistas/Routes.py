#################################################
# Web API Entrevistas
# Mapeamento de Rotas
#################################################

from flask import jsonify, request
from Server import App, Response

@App.route("/entrevistas", methods=["GET"])
def ListarEntrevistas():
    from Entevistas.Services.ListarEntrevista import ListarEntrevista
    Dados = ListarEntrevista()
    Response["Dados"] = {"Candidatos":Dados}
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/entrevistas/<int:Id>", methods=["GET"])
def ConsultarPorId(Id):
    from Entevistas.Services.ConsultarPorId import ConsultarPorId
    Dados = ConsultarPorId(Id)
    Response["Dados"] = Dados
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)


@App.route("/entrevistas", methods=["POST"])
def CadastrarEntrevista():
    from Entevistas.Services.CadastrarEntrevista import CadastrarEntrevista

    Dados = request.get_json()
    Id = Dados["Id"]
    DataEntrevista = Dados["DataEntrevista"]
    CodCandidato = Dados["CodCandidato"]
    CodVaga = Dados["CodVaga"]
    CodFuncionario = Dados["CodFuncionario"]
    StatusResultado = ["StatusResultado"]
    CadastrarEntrevista(Id, DataEntrevista, CodCandidato, CodVaga, CodFuncionario, StatusResultado)
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/entrevistas", methods=["PUT"])
def AtualizarEntrevistas():
    from Entevistas.Services.AtualizarEntrevista import AtualizarEntrevista

    Dados = request.get_json()
    Id = Dados["Id"]
    DataEntrevista = Dados["DataEntrevista"]
    CodCandidato = Dados["CodCandidato"]
    CodVaga = Dados["CodVaga"]
    CodFuncionario = Dados["CodFuncionario"]
    StatusResultado = ["StatusResultado"]
    AtualizarEntrevista(Id, DataEntrevista, CodCandidato, CodVaga, CodFuncionario, StatusResultado)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/entrevistas/<int:Id>", methods=["DELETE"])
def InativarEntrevista(Id):
    from Entevistas.Services.InativarEntrevista import InativarEntrevista
    InativarEntrevista(Id)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)




