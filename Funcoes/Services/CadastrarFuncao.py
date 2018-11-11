#################################################
# Web API Funções
# Cadastro de Funções
#################################################

from Funcoes.Models.Funcoes import Funcoes

def CadastrarFuncao(Id, Nome, Nivel):
    Funcoes.append({"Id":Id, "Nome":Nome, "Nivel":Nivel, "Ativo":True})
    return