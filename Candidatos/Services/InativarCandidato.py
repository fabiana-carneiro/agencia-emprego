#################################################
# Web API Candidatos
# Inativação de Candidato
#################################################

from Candidatos.Models.Candidatos import Candidatos
from Candidatos.Services.ConsultarPorId import ConsultarPorId

def InativarCandidato(Id):
    CandidatoAlterar = ConsultarPorId(Id)

    if CandidatoAlterar is None:
        return False
    else:
        CandidatoAlterar["Ativo"] = False
        return True