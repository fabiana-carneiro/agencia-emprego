#################################################
# Web API Cidades
# Atualização de cidade
#################################################

from Cidades.Models.Cidades import Cidades
from Cidades.Services.ConsultarPorId import ConsultarPorId

def AtualizarCidade(Id, Nome, Bairro, Uf, Ativo):
    CidadeAlterar = ConsultarPorId(Id)

    if CidadeAlterar is None:
        return False
    else:
        CidadeAlterar["Nome"] = Nome
        CidadeAlterar["Bairro"] = Bairro
        CidadeAlterar["Uf"] = Uf
        CidadeAlterar["Ativo"] = Ativo
        return True