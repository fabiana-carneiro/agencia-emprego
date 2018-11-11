#################################################
# Web API Professores
# Consulta de professor por Id
#################################################

from Professores.Models.Professores import Professores

def ConsultarPorId(Id):
    Professor = {}

    for Professor in Professores:
        if Professor["Id"] == Id:
            break
        else:
            Professor = {}
    return Professor

