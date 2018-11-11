#################################################
# Web API Cidadess
# Cadastro de Cidades
#################################################
from Cidades.Models.Cidades import Cidades

def CadastrarCidades(Id, Nome, Bairro, Uf):
    Cidades.append({"Id":Id, "Nome":Nome, "Bairro":Bairro, "Uf":Uf, "Ativo":True})
    return
