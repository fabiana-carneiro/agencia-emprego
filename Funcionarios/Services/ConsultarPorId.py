#################################################
# Web API Funcionarios
# Consulta de funcionario por Id
#################################################

from Funcionarios.Models.Funcionarios import Funcionarios

def ConsultarPorId(Id):
    Funcionario = {}
    for Funcionario in Funcionarios:
        if Funcionario["Id"] == Id:
            break
        else:
            Funcionario = {}
    return Funcionario