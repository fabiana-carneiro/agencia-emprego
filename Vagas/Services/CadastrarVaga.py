#################################################
# Web API Funções
# Cadastro de Funções
#################################################
from Vagas.Models.Vagas import Vagas


def CadastrarVaga(Id, Descricao, Salario, Escolaridade, CodCliente, CodFuncao):
    Vagas.append({"Id":Id, "Descricao":Descricao, "Salario":Salario, "Escolaridade":Escolaridade,
                  "CodCliente":CodCliente, "CodFuncao":CodFuncao, "Ativo": True})

