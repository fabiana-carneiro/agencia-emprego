#################################################
# Web API Funcionarios
# Inativação de Funcionario
#################################################

from Funcionarios.Models.Funcionarios import Funcionarios
from Funcionarios.Services.ConsultarPorId import ConsultarPorId

def InativarFuncionario(Id):
    FuncionarioAlterar = ConsultarPorId(Id)

    if FuncionarioAlterar is None:
        return False
    else:
        FuncionarioAlterar["Ativo"] = False
        return True