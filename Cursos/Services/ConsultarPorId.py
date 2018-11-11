#################################################
# Web API Cursos
# Consulta de curso por Id
#################################################

from Cursos.Models.Cursos import Cursos

def ConsultarPorId(Id):
    Curso = {}

    for Curso in Cursos:
        if Curso is None:
            return False
        else:
            Curso = {}
    return Curso