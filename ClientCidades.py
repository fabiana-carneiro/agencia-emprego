def cadastrar_cidade():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    Nome = input("Digite o nome: ")
    Bairro = input("Digite o bairro: ")
    Uf = input("Digite a sigla do Estado: ")
    dados = {"Codigo":Codigo, "Nome":Nome, "Bairro":Bairro, "Uf":Uf}

    url = "http://localhost/cidades"
    Dados = Req.api.post(url, json=dados).json()
    print(Dados)


def deletar_cidade():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    url = "http://localhost/cidades/" + str(Codigo)
    Dados = Req.api.delete(url).json()
    print(Dados)


def atualizar_cidade():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    Nome = input("Digite o nome: ")
    Bairro = input("Digite o bairro: ")
    Uf = input("Digite a sigla do Estado: ")
    dados = {"Codigo": Codigo, "Nome": Nome, "Bairro": Bairro, "Uf": Uf}

    url = "http://localhost/cidades"
    Dados = Req.api.put(url, json=dados).json()
    print(Dados)


def menu():
    while True:
        print("Digite 1 para cadastrar cidade")
        print("Digite 2 para deletar cidade")
        print("Digite 3 para atualizar cidade")
        print("Digite SAIR para sair")
        num = input("Digite sua escolha: ")
        if num == 'SAIR' or num == 'sair':
            return
        if num == '1':
            cadastrar_cidade()
        if num == '2':
            deletar_cidade()
        elif num == '3':
            atualizar_cidade()
        else:
            print("Ei, por favor, escolha uma opção válida!")


menu()