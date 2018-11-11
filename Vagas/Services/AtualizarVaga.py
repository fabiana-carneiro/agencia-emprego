#################################################
# Web API Vagas
# Atualização de vagas
#################################################

from Vagas.Models.Vagas import Vagas
from Vagas.Services.ConsultarPorId import ConsultarPorId

def AtualizarVaga(Id, Descricao, Salario, Escolaridade, CodCliente, CodFuncao, Ativo):
    VagaAlterar = ConsultarPorId(Id)

    if VagaAlterar is None:
        return False
    else:
        VagaAlterar["Descricao"] = Descricao
        VagaAlterar["Salario"] = Salario
        VagaAlterar["Escolaridade"] = Escolaridade
        VagaAlterar["CodCliente"] = CodCliente
        VagaAlterar["CodFuncao"] = CodFuncao
        VagaAlterar["Ativo"] = Ativo
        return True