#################################################
# Web API Funcionarios
# Cadastro de Funcionarios
#################################################

from Funcionarios.Models.Funcionarios import Funcionarios

def CadastrarFuncionario(Id, Matricula, Nome, Cpf, DataNascimento, Email, DataInicio, CodEndereco, CodFuncao):
    Funcionarios.append({"Id":Id, "Matricula": Matricula, "Nome":Nome, "Cpf":Cpf, "DataNascimento": DataNascimento,
                         "Email":Email, "DataInicio": DataInicio, "CodEndereco": CodEndereco, "CodFuncao": CodFuncao, "Ativo": True})
    return