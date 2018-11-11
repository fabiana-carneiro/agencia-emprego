#################################################
# Web API Entrevistas
# Consulta de entrevista por ID
#################################################

from Entevistas.Models.Entrevistas import Entrevistas

def ConsultarPorId(Id):
    Entrevista = {}

    for Entrevista in Entrevistas:
        if Entrevista["Id"] == Id:
            break
        else:
            Entrevista = {}
    return Entrevista
