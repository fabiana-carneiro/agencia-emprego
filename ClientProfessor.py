def cadastrar_professor():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    Nome = input("Digite o nome: ")
    Idade = int(input("Digite a idade: "))
    Cpf = input("Digite o CPF: ")
    dados = {"Codigo":Codigo, "Nome":Nome, "Idade":Idade, "Cpf":Cpf}

    url = "http://localhost/professores"
    Dados = Req.api.post(url, json=dados).json()
    print(Dados)


def deletar_professor():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    url = "http://localhost/professores/" + str(Codigo)
    Dados = Req.api.delete(url).json()
    print(Dados)


def atualizar_professor():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    Nome = input("Digite o nome: ")
    Idade = int(input("Digite a idade: "))
    Cpf = input("Digite o CPF: ")
    dados = {"Codigo": Codigo, "Nome": Nome, "Idade": Idade, "Cpf": Cpf}

    url = "http://localhost/professores"
    Dados = Req.api.put(url, json=dados).json()
    print(Dados)


def menu():
    while True:
        print("Digite 1 para cadastrar professores")
        print("Digite 2 para deletar professores")
        print("Digite 3 para atualizar professores")
        print("Digite SAIR para sair")
        num = input("Digite sua escolha: ")
        if num == 'SAIR' or num == 'sair':
            return
        if num == '1':
            cadastrar_professor()
        if num == '2':
            deletar_professor()
        elif num == '3':
            atualizar_professor()
        else:
            print("Ei, por favor, escolha uma opção válida!")


menu()