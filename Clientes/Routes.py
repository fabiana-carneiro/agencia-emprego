#################################################
# Web API Clientes
# Mapeamento de Rotas
#################################################

from flask import jsonify, request
from Server import App, Response

@App.route("/clientes", methods=["GET"])
def ListarClientes():
    from Clientes.Services.ListarClientes import ListarClientes
    Dados = ListarClientes()
    Response["Dados"] = {"Clientes":Dados}
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/clientes/<int:Id>", methods=["GET"])
def ConsultarPorId(Id):
    from Clientes.Services.ConsultarPorId import ConsultarPorId
    Dados = ConsultarPorId(Id)
    Response["Dados"] = Dados
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/clientes", methods=["POST"])
def CadastrarCliente():
    from Clientes.Services.CadastrarCliente import CadastrarCliente

    Dados = request.get_json()
    Id = Dados["Id"]
    NomeFantasia = Dados["NomeFantasia"]
    RazaoSocial = Dados["RazaoSocial"]
    Segmento = Dados["Segmento"]
    Cnpj = Dados["Cnpj"]
    Telefone = Dados["Telefone"]
    CodEndereco = Dados["CodEndereco"]
    CadastrarCliente(Id, NomeFantasia, RazaoSocial, Segmento, Cnpj, Telefone,  CodEndereco)
    
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/clientes", methods=["PUT"])
def AtualizarCliente():
    from Clientes.Services.AtualizarCliente import AtualizarCliente
    
    Dados = request.get_json()
    Id = Dados["Id"]
    NomeFantasia = Dados["NomeFantasia"]
    RazaoSocial = Dados["RazaoSocial"]
    Segmento = Dados["Segmento"]
    Cnpj = Dados["Cnpj"]
    Telefone = Dados["Telefone"]
    CodEndereco = Dados["CodEndereco"]
    Ativo = Dados["Ativo"]
    AtualizarCliente(Id, NomeFantasia, RazaoSocial, Segmento, Cnpj, Telefone, CodEndereco, Ativo)
    
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/clientes/<int:Id>", methods=["DELETE"])
def InativarCliente(Id):
    from Clientes.Services.InativarCliente import InativarCliente
    InativarCliente(Id)
    
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)