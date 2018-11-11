#################################################
# Web API Vagas
# Consulta de vaga por Id
#################################################

from Vagas.Models.Vagas import Vagas

def ConsultarPorId(Id):
    Vaga = {}

    for Vaga in Vagas:
        if Vaga["Id"] == Id:
            break
        else:
            Vaga = {}
    return Vaga