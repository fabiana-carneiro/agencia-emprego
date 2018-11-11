def cadastrar_funcionario():
    import requests as Req
        
    Codigo = int(input("Digite o código: "))
    Matricula = input("Digite a matricula: ")
    Nome = input("Digite o nome: ")
    Cpf = input("Digite o CPF: ")
    DataNascimento = input("Digite a data de nascimento: ")
    Email = input("Digite o email: ")
    DataInicio = input("Digite a data de início: ")
    CodEndereco = int(input("Digite o código do endereço: "))
    CodFuncao = int(input("Digite o código da função: "))
    dados = {"Codigo": Codigo, "Matricula": Matricula, "Nome": Nome, "Cpf": Cpf, "Email": Email,
             "DataInicio": DataInicio, "CodEndereco": CodEndereco, "CodFuncao": CodFuncao}

    url = "http://localhost/funcionarios"
    Dados = Req.api.post(url, json=dados).json()
    print(Dados)

def deletar_funcionario():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    url = "http://localhost/funcionarios/" + str(Codigo)
    Dados = Req.api.delete(url).json()
    print(Dados)

def atualizar_funcionario():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    Matricula = input("Digite a matricula: ")
    Nome = input("Digite o nome: ")
    Cpf = input("Digite o CPF: ")
    DataNascimento = input("Digite a data de nascimento: ")
    Email = input("Digite o email: ")
    DataInicio = input("Digite a data de início: ")
    CodEndereco = int(input("Digite o código do endereço: "))
    CodFuncao = int(input("Digite o código da função: "))
    dados = {"Codigo": Codigo, "Matricula": Matricula, "Nome": Nome, "Cpf": Cpf, "Email": Email,
             "DataInicio": DataInicio, "CodEndereco": CodEndereco, "CodFuncao": CodFuncao}

    url = "http://localhost/funcionarios"
    Dados = Req.api.put(url, json=dados).json()
    print(Dados)

def menu():
    while True:
        print("Digite 1 para cadastrar funcionario")
        print("Digite 2 para deletar funcionario")
        print("Digite 3 para atualizar funcionario")
        print("Digite SAIR para sair")
        num = input("Digite sua escolha: ")
        if num == 'SAIR' or num == 'sair':
            return
        if num == '1':
            cadastrar_funcionario()
        if num == '2':
            deletar_funcionario()
        elif num == '3':
            atualizar_funcionario()
        else:
            print("Ei, por favor, escolha uma opção válida!")
menu()