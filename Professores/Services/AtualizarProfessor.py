#################################################
# Web API Professores
# Atualização de professor
#################################################

from Professores.Models.Professores import Professores
from Professores.Services.ConsultarPorId import ConsultarPorId


def AtualizarProfessor(Id, Nome, Idade, Cpf, Ativo):
    ProfessorAlterar = ConsultarPorId(Id)

    if ProfessorAlterar is None:
        return False
    else:
        ProfessorAlterar["Nome"] = Nome
        ProfessorAlterar["Idade"] = Idade
        ProfessorAlterar["Cpf"] = Cpf
        ProfessorAlterar["Ativo"] = Ativo
        return True