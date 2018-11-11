#################################################
# Web API Candidatos
# Consulta de candidato por Id
#################################################

from Candidatos.Models.Candidatos import Candidatos

def ConsultarPorId(Id):
    Candidato = {}
    for Candidato in Candidatos:
        if Candidato["Id"] == Id:
            break
        else:
            Candidato = {}
    return Candidato