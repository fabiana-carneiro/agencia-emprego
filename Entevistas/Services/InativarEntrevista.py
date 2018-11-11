#################################################
# Web API Entrevistas
# Inativação de Entrevista
#################################################
from Entevistas.Models.Entrevistas import Entrevistas
from Entevistas.Services.ConsultarPorId import ConsultarPorId


def InativarEntrevista(Id):
    EntrevistaAlterar = ConsultarPorId(Id)

    if EntrevistaAlterar is None:
        return False
    else:
        EntrevistaAlterar["Ativo"] = False
        return True

