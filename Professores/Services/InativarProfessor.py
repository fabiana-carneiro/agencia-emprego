#################################################
# Web API Professores
# Inativação de Professor
#################################################
from Professores.Models.Professores import Professores

from Professores.Services.ConsultarPorId import ConsultarPorId


def InativarProfessor(Id):
    ProfessorAlterar = ConsultarPorId(Id)

    if ProfessorAlterar is None:
        return False
    else:
        ProfessorAlterar["Ativo"] = False
        return True