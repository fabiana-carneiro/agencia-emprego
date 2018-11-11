#################################################
# Web API Professores
# Cadastro de Professores
#################################################

from Professores.Models.Professores import Professores

def CadastrarProfessor(Id, Nome, Idade, Cpf):
    Professores.append({"Id":Id, "Nome":Nome, "Idade":Idade, "Cpf":Cpf, "Ativo":True})
    return

