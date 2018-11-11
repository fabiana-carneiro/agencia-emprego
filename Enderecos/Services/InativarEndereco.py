#################################################
# Web API Endereços
# Inativação de Endereços
#################################################

from Enderecos.Models.Enderecos import Enderecos
from Enderecos.Services.ConsultarPorId import ConsultarPorId

def InativarEndereco(Id):
    EnderecoAlterar = ConsultarPorId(Id)

    if EnderecoAlterar is None:
        return False
    else:
        EnderecoAlterar["Ativo"] = False
        return True