def cadastrar_funcao():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    Nome = input("Digite o nome: ")
    Nivel = input("Digite o Nivel: ")
    dados = {"Codigo":Codigo, "Nome":Nome, "Nivel":Nivel}

    url = "http://localhost/funcoes"
    Dados = Req.api.post(url, json=dados).json()
    print(Dados)

def deletar_funcao():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    url = "http://localhost/funcoes/" + str(Codigo)
    Dados = Req.api.delete(url).json()
    print(Dados)

def atualizar_funcao():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    Nome = input("Digite o nome: ")
    Nivel = input("Digite o Nivel: ")
    dados = {"Codigo": Codigo, "Nome": Nome, "Nivel": Nivel}

    url = "http://localhost/funcoes"
    Dados = Req.api.put(url, json=dados).json()
    print(Dados)

def menu():
    while True:
        print("Digite 1 para cadastrar cliente")
        print("Digite 2 para deletar cliente")
        print("Digite 3 para atualizar cliente")
        print("Digite SAIR para sair")
        num = input("Digite sua escolha: ")
        if num == 'SAIR' or num == 'sair':
            return
        if num == '1':
            cadastrar_funcao()
        if num == '2':
            deletar_funcao()
        elif num == '3':
            atualizar_funcao()
        else:
            print("Ei, por favor, escolha uma opção válida!")
menu()

