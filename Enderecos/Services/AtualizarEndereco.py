#################################################
# Web API Endereços
# Atualização de Endereço
#################################################

from Enderecos.Models.Enderecos import Enderecos
from Enderecos.Services.ConsultarPorId import ConsultarPorId

def AtualizarEndereco(Id, Logradouro, Numero, Cep, CodCidade, Ativo):
    EnderecoAlterar = ConsultarPorId(Id)

    if EnderecoAlterar is None:
        return False
    else:
        EnderecoAlterar["Logradouro"] = Logradouro
        EnderecoAlterar["Numero"] = Numero
        EnderecoAlterar["Cep"] = Cep
        EnderecoAlterar["CodCidade"] = CodCidade
        EnderecoAlterar["Ativo"] = Ativo
        return True