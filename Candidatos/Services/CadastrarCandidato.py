#################################################
# Web API Candidatos
# Cadastro de Candidatos
#################################################

from Candidatos.Models.Candidatos import Candidatos

def CadastrarCandidato(Id, Nome, Cpf, Escolaridade, Telefone, Email):
    Candidatos.append({"Id":Id, "Nome":Nome, "Cpf":Cpf, "Escolaridade":Escolaridade, "Telefone":Telefone,"Email":Email, "Ativo": True})
    return