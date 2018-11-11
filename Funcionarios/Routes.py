#################################################
# Web API Funcaionarios
# Mapeamento de Rotas
#################################################

from flask import jsonify, request
from Server import App, Response

@App.route("/funcionarios", methods=["GET"])
def ListarFuncionarios():
    from Funcionarios.Services.ListarFuncionario import ListarFuncionarios
    Dados = ListarFuncionarios()
    Response["Dados"] = {"Funcionarios":Dados}
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/funcionarios/<int:Id>", methods=["GET"])
def ConsultarPorId(Id):
    from Funcionarios.Services.ConsultarPorId import ConsultarPorId
    Dados = ConsultarPorId(Id)
    Response["Dados"] = Dados
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/funcionarios", methods=["POST"])
def CadastrarFuncionario():
    from Funcionarios.Services.CadastrarFuncionario import CadastrarFuncionario
    
    Dados = request.get_json()
    Id = Dados["Id"]
    Matricula = Dados["Matricula"]
    Nome = Dados["Nome"]
    Cpf = Dados["Cpf"]
    DataNascimento = Dados["DataNascimento"]
    Email = Dados["Email"]
    DataInicio = Dados["DataInicio"]
    CodEndereco = Dados["CodEndereco"]
    CodFuncao = Dados["CodFuncao"]
    CadastrarFuncionario(Id, Matricula, Nome, Cpf, DataNascimento, Email, DataInicio, CodEndereco, CodFuncao)
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/funcionarios", methods=["PUT"])
def AtualizarCandidato():
    from Funcionarios.Services.AtualizarFuncionario import AtualizarFuncionario
    
    Dados = request.get_json()
    Id = Dados["Id"]
    Matricula = Dados["Matricula"]
    Nome = Dados["Nome"]
    Cpf = Dados["Cpf"]
    DataNascimento = Dados["DataNascimento"]
    Email = Dados["Email"]
    DataInicio = Dados["DataInicio"]
    CodEndereco = Dados["CodEndereco"]
    CodFuncao = Dados["CodFuncao"]
    Ativo = Dados["Ativo"]
    AtualizarFuncionario(Id, Matricula, Nome, Cpf, DataNascimento, Email, DataInicio, CodEndereco, CodFuncao, Ativo)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/funcionarios/<int:Id>", methods=["DELETE"])
def InativarCandidato(Id):
    from Candidatos.Services.InativarCandidato import InativarCandidato    
    InativarCandidato(Id)
    
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)