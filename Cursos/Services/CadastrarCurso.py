#################################################
# Web API Cursos
# Cadastro de Cursos
#################################################
from Cursos.Models.Cursos import Cursos


def CadastrarCurso(Id, Nome, Duracao, CodProfessor):
    Cursos.append({"Id":Id, "Nome":Nome, "Duracao":Duracao, "CodProfessor":CodProfessor, "Ativo":True})
    return

