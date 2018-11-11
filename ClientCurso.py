def cadastrar_curso():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    Nome = input("Digite o nome: ")
    Duracao = int(input("Digite o CPF: "))
    CodProfessor = int(input("Digite a escolaridade: "))
    dados = {"Codigo":Codigo, "Nome":Nome, "Durracao":Duracao, "CodProfessor":CodProfessor}

    url = "http://localhost/cursos"
    Dados = Req.api.post(url, json=dados).json()
    print(Dados)


def deletar_curso():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    url = "http://localhost/cursos/" + str(Codigo)
    Dados = Req.api.delete(url).json()
    print(Dados)


def atualizar_curso():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    Nome = input("Digite o nome: ")
    Duracao = int(input("Digite o CPF: "))
    CodProfessor = int(input("Digite a escolaridade: "))
    dados = {"Codigo": Codigo, "Nome": Nome, "Durracao": Duracao, "CodProfessor": CodProfessor}

    url = "http://localhost/cursos"
    Dados = Req.api.put(url, json=dados).json()
    print(Dados)


def menu():
    while True:
        print("Digite 1 para cadastrar curso")
        print("Digite 2 para deletar curso")
        print("Digite 3 para atualizar curso")
        print("Digite SAIR para sair")
        num = input("Digite sua escolha: ")
        if num == 'SAIR' or num == 'sair':
            return
        if num == '1':
            cadastrar_curso()
        if num == '2':
            deletar_curso()
        elif num == '3':
            atualizar_curso()
        else:
            print("Ei, por favor, escolha uma opção válida!")


menu()