#################################################
# Web API Clientes
# Inativação de Cliente
#################################################

from Clientes.Models.Clientes import Clientes
from Clientes.Services.ConsultarPorId import ConsultarPorId

def InativarCliente(Id):
    ClienteAlterar = ConsultarPorId(Id)

    if ClienteAlterar is None:
        return False
    else:
        ClienteAlterar["Ativo"] = False
        return True