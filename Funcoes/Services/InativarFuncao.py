#################################################
# Web API Funções
# Inativação de Função
#################################################

from Funcoes.Models.Funcoes import Funcoes
from Funcoes.Services.ConsultarPorId import ConsultarPorId

def InativarFuncao(Id):
    FuncaoAlterar = ConsultarPorId(Id)

    if FuncaoAlterar is None:
        return False
    else:
        FuncaoAlterar["Ativo"] = False
        return True