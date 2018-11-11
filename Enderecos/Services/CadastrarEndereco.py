#################################################
# Web API Endereços
# Cadastro de Endereços		
#################################################

from Enderecos.Models.Enderecos import Enderecos

def CadastrarEndereco(Id, Logradouro, Numero, Cep, CodCidade):
    Enderecos.append({"Id":Id, "Logradouro":Logradouro, "Numero":Numero, "Cep":Cep, "CodCidade":CodCidade, "Ativo":True})
    return

