def cadastrar_candidato():
    import requests as Req
        
    Codigo = int(input("Digite o código: "))
    Nome = input("Digite o nome: ")
    Cpf = input("Digite o CPF: ")
    Escolaridade = input("Digite a escolaridade: ")
    Telefone = input("Digite o telefone: ")
    Email = input("Digite o email: ")
    dados = {"Codigo": Codigo, "Nome": Nome, "Cpf": Cpf, "Escolaridade": Escolaridade, "Telefone": Telefone, "Email": Email}
    
    url = "http://localhost/candidatos"
    Dados = Req.api.post(url, json=dados).json()
    print(Dados)

def deletar_candidato():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    url = "http://localhost/candidatos/" + str(Codigo)
    Dados = Req.api.delete(url).json()
    print(Dados)

def atualizar_candidato():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    Nome = input("Digite o nome: ")
    Cpf = input("Digite o CPF: ")
    Escolaridade = input("Digite a escolaridade: ")
    Telefone = input("Digite o telefone: ")
    Email = input("Digite o email: ")
    dados = {"Codigo": Codigo, "Nome": Nome, "Cpf": Cpf, "Escolaridade": Escolaridade, "Telefone": Telefone, "Email": Email}

    url = "http://localhost/candidatos"
    Dados = Req.api.put(url, json=dados).json()
    print(Dados)

def menu():
    while True:
        print("Digite 1 para cadastrar candidato")
        print("Digite 2 para deletar candidato")
        print("Digite 3 para atualizar candidato")
        print("Digite SAIR para sair")
        num = input("Digite sua escolha: ")
        if num == 'SAIR' or num == 'sair':
            return
        if num == '1':
            cadastrar_candidato()
        if num == '2':
            deletar_candidato()
        elif num == '3':
            atualizar_candidato()
        else:
            print("Ei, por favor, escolha uma opção válida!")
menu()