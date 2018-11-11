#################################################
# Web API Cursos
# Atualização de curso
#################################################

from Cursos.Models.Cursos import Cursos
from Cursos.Services.ConsultarPorId import ConsultarPorId

def AtualizarCurso(Id, Nome, Duracao, CodProfessor, Ativo):
    CursoAlterar = ConsultarPorId(Id)

    if CursoAlterar is None:
        return False
    else:
        CursoAlterar["Nome"] = Nome
        CursoAlterar["Duracao"] = Duracao
        CursoAlterar["CodProfessor"] = CodProfessor
        CursoAlterar["Ativo"] = Ativo
        return True