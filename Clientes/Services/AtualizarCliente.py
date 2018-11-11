#################################################
# Web API Clientes
# Atualização de cliente
#################################################

from Clientes.Models.Clientes import Clientes
from Clientes.Services.ConsultarPorId import ConsultarPorId

def AtualizarCliente(Id, NomeFantasia, RazaoSocial, Segmento, Cnpj, Telefone,  CodEndereco, Ativo):
    ClienteAlterar = ConsultarPorId(Id)

    if ClienteAlterar is None:
        return False
    else:
        ClienteAlterar["NomeFantasia"] = NomeFantasia
        ClienteAlterar["RazaoSocial"] = RazaoSocial
        ClienteAlterar["Segmento"] = Segmento
        ClienteAlterar["Cnpj"] = Cnpj
        ClienteAlterar["Telefone"] = Telefone
        ClienteAlterar["CodEndereco"] = CodEndereco
        ClienteAlterar["Ativo"] = Ativo
        return True