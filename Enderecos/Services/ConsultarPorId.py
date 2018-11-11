#################################################
# Web API Endereços
# Consulta de endereço por Id
#################################################

from Enderecos.Models.Enderecos import Enderecos

def ConsultarPorId(Id):
    Endereco = {}
    for Endereco in Enderecos:
        if Endereco["Id"] == Id:
            break
        else:
            Endereco = {}
    return Endereco