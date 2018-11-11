#################################################
# Web API Funções
# Consulta de função por Id
#################################################

from Funcoes.Models.Funcoes import Funcoes

def ConsultarPorId(Id):
    Funcao = {}
    for Funcao in Funcoes:
        if Funcao["Id"] == Id:
            break
        else:
            Funcao = {}
    return Funcao