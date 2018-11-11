#################################################
# Web API Cidades
# Consulta de cidade por Id
#################################################
from Cidades.Models.Cidades import Cidades


def ConsultarPorId(Id):
    Cidade = {}

    for Cidade in Cidades:
        if Cidade["Id"] == Id:
            break
        else:
            Cidade = {}
    return Cidade
