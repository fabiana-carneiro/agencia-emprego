def cadastrar_vaga():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    Descricao = input("Digite a descriçao da vaga: ")
    Salario = float(input("Digite o salário RS: "))
    Escolaridade = input("Digite a escolaridade: ")
    CodCliente = int(input("Digite o código do cliente que está ofertando a vaga: "))
    CodFuncao = int(input("Digite o código da  função: "))
    dados = {"Codigo":Codigo, "Descricao":Descricao, "Salario":Salario, "Escolaridade":Escolaridade,
                  "CodCliente":CodCliente, "CodFuncao":CodFuncao}

    url = "http://localhost/vagas"
    Dados = Req.api.post(url, json=dados).json()
    print(Dados)

def deletar_vaga():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    url = "http://localhost/vagas/" + str(Codigo)
    Dados = Req.api.delete(url).json()
    print(Dados)

def atualizar_vaga():
    import  requests as Req

    Codigo = int(input("Digite o código: "))
    Descricao = input("Digite a descriçao da vaga: ")
    Salario = float(input("Digite o salário RS: "))
    Escolaridade = input("Digite a escolaridade: ")
    CodCliente = int(input("Digite o código do cliente que está ofertando a vaga: "))
    CodFuncao = int(input("Digite o código da  função: "))
    dados = {"Codigo": Codigo, "Descricao": Descricao, "Salario": Salario, "Escolaridade": Escolaridade,
             "CodCliente": CodCliente, "CodFuncao": CodFuncao}

    url = "http://localhost/vagas"
    Dados = Req.api.put(url, json=dados).json()
    print(Dados)

def menu():
    while True:
        print("Digite 1 para cadastrar vaga")
        print("Digite 2 para deletar vaga")
        print("Digite 3 para atualizar vaga")
        print("Digite SAIR para sair")
        num = input("Digite sua escolha: ")
        if num == 'SAIR' or num == 'sair':
            return
        if num == '1':
            cadastrar_vaga()
        if num == '2':
            deletar_vaga()
        elif num == '3':
            atualizar_vaga()
        else:
            print("Ei, por favor, escolha uma opção válida!")
menu()