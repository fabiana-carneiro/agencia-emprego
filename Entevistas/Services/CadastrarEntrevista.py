#################################################
# Web API Candidatos
# Cadastro de Entrevistas
#################################################

from Entevistas.Models.Entrevistas import Entrevistas

def CadastrarEntrevista(Id, DataEntrevista, CodCandidato,  CodVaga, CodFuncionario, StatusResultado):
    Entrevistas.append({"Id":Id, "DataEntrevista":DataEntrevista, "CodCandidato":CodCandidato, "CodVaga":CodVaga,
                        "CodFuncionario":CodFuncionario, "StatusResultado":StatusResultado, "Ativo": True})
    return
