#################################################
# Web API Enderecos
# Mapeamento de Rotas
#################################################

from flask import jsonify, request
from Server import App, Response

@App.route("/enderecos", methods=["GET"])
def ListarEnderecos():
    from Enderecos.Services.ListarEnderecos import ListarEnderecos
    Dados = ListarEnderecos()
    Response["Dados"] = {"Enderecos":Dados}
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/enderecos/<int:Id>", methods=["GET"])
def ConsultarPorId(Id):
    from Enderecos.Services.ConsultarPorId import ConsultarPorId
    Dados = ConsultarPorId(Id)
    Response["Dados"] = Dados
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/enderecos", methods=["POST"])
def CadastrarEndereco():
    from Enderecos.Services.CadastrarEndereco import CadastrarEndereco
    
    Dados = request.get_json()
    Id = Dados["Id"]
    Logradouro = Dados["Logradouro"]
    Numero = Dados["Numero"]
    Cep = Dados["Cep"]
    CodCidade = Dados["CodCidade"]
    CadastrarEndereco(Id, Logradouro, Numero, Cep, CodCidade)
    
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/enderecos", methods=["PUT"])
def AtualizarEndereco():
    from Enderecos.Services.AtualizarEndereco import AtualizarEndereco 

    Dados = request.get_json()
    Id = Dados["Id"]
    Logradouro = Dados["Logradouro"]
    Numero = Dados["Numero"]
    Cep = Dados["Cep"]
    CodCidade = Dados["CodCidade"]
    AtualizarEndereco(Id, Logradouro, Numero, Cep, CodCidade)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/enderecos/<int:Id>", methods=["DELETE"])
def InativarEndereco(Id):
    from Enderecos.Services.InativarEndereco import InativarEndereco    
    InativarEndereco(Id)
    
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)