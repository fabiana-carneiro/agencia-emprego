#################################################
# Web API Entrevistas
# Atualização de entrevista
#################################################

from Entevistas.Models.Entrevistas import Entrevistas
from Entevistas.Services.ConsultarPorId import ConsultarPorId


def AtualizarEntrevista(Id, DataEntrevista, CodCandidato,  CodVaga, CodFuncionario, StatusResultado, Ativo):
    EntrevistaAlterar = ConsultarPorId(Id)

    if EntrevistaAlterar is None:
        return False
    else:
        EntrevistaAlterar["DataEntrevista"] = DataEntrevista
        EntrevistaAlterar["CodCandidato"] = CodCandidato
        EntrevistaAlterar["CodVaga"] = CodVaga
        EntrevistaAlterar["CodFuncionario"] = CodFuncionario
        EntrevistaAlterar["StatusResultado"] = StatusResultado
        EntrevistaAlterar["Ativo"] = Ativo
        return True