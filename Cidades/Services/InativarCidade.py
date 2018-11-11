#################################################
# Web API Candidatos
# Inativação de Candidato
#################################################

from Cidades.Models.Cidades import Cidades
from Cidades.Services.ConsultarPorId import ConsultarPorId


def InativarCidade(Id):
    CidadeAlterar = ConsultarPorId(Id)

    if CidadeAlterar is None:
        return False
    else:
        CidadeAlterar["Ativo"] == False
        return True