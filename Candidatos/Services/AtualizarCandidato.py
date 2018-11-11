#################################################
# Web API Candidatos
# Atualização de candidato
#################################################

from Candidatos.Models.Candidatos import Candidatos
from Candidatos.Services.ConsultarPorId import ConsultarPorId

def AtualizarCandidato(Id, Nome, Cpf, Escolaridade, Telefone, Email, Ativo):
    CandidatoAlterar = ConsultarPorId(Id)

    if CandidatoAlterar is None:
        return False
    else:
        CandidatoAlterar["Nome"] = Nome
        CandidatoAlterar["Cpf"] = Cpf
        CandidatoAlterar["Escolaridade"] = Escolaridade
        CandidatoAlterar["Telefone"] = Telefone
        CandidatoAlterar["Email"] = Email
        CandidatoAlterar["Ativo"] = Ativo
        return True
