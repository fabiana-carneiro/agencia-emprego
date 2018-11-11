#################################################
# Web API Cursos
# Inativação de Curso
#################################################

from Cursos.Models.Cursos import Cursos
from Cursos.Services.ConsultarPorId import ConsultarPorId


def InativarCurso(Id):
    CursoAlterar = ConsultarPorId(Id)

    if CursoAlterar is None:
        return True
    else:
        CursoAlterar["Ativo"] = False
        return True