#################################################
# Web API Clientes
# Cadastro de Clientes
#################################################

from Clientes.Models.Clientes import Clientes

def CadastrarCliente(Id, NomeFantasia, RazaoSocial, Segmento, Cnpj, Telefone,  CodEndereco):
    Clientes.append({"Id":Id, "NomeFantasia":NomeFantasia, "RazaoSocial":RazaoSocial, "Segmento":Segmento,
                     "Cnpj":Cnpj, "Telefone":Telefone, "CodEndereco":CodEndereco, "Ativo":True})
    return
