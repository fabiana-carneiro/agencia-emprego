#################################################
# Web API Vagas
# Inativação de Vaga
#################################################

from Vagas.Models.Vagas import Vagas
from Vagas.Services.ConsultarPorId import ConsultarPorId


def InativarVaga(Id):
    VagaAlterar = ConsultarPorId(Id)

    if VagaAlterar is None:
        return False
    else:
        VagaAlterar["Ativo"] = False
        return True