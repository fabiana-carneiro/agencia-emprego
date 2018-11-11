#################################################
# Web API Funções
# Atualização de função
#################################################

from Funcoes.Models.Funcoes import Funcoes
from Funcoes.Services.ConsultarPorId import ConsultarPorId

def AtualizarFuncao(Id, Nome, Nivel, Ativo):
    FuncaoAlterar = ConsultarPorId(Id)

    if FuncaoAlterar is None:
        return False
    else:
        FuncaoAlterar["Nome"] = Nome
        FuncaoAlterar["Nivel"] = Nivel
        FuncaoAlterar["Ativo"] = Ativo
        return True