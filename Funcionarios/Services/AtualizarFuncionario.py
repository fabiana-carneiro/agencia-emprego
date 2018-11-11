#################################################
# Web API Funcionarios
# Atualização de funcionarios
#################################################

from Funcionarios.Models.Funcionarios import Funcionarios
from Funcionarios.Services.ConsultarPorId import ConsultarPorId

def AtualizarFuncionario(Codigo, Matricula, Nome, Cpf, DataNascimento, Email, DataInicio, CodEndereco, CodFuncao, Ativo):
    FuncionarioAlterar = ConsultarPorId(Codigo)

    if FuncionarioAlterar is None:
        return False
    else:
    	FuncionarioAlterar["Matricula"] = Matricula
        FuncionarioAlterar["Nome"] = Nome
        FuncionarioAlterar["Cpf"] = Cpf
        FuncionarioAlterar["DataNascimento"] = DataNascimento
        FuncionarioAlterar["Email"] = Email
        FuncionarioAlterar["DataInicio"] = DataInicio
        FuncionarioAlterar["CodEndereco"] = CodEndereco
        FuncionarioAlterar["CodFuncao"] = CodFuncao
        FuncionarioAlterar["Ativo"] = Ativo
        return True