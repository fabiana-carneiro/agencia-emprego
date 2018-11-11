from datetime import date

def cadastrar_entrevista():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    DataEntrevista = date(input("Digite a data da entrevista: "))
    CodCandidato = int(input("Digite o código do candidato: "))
    CodVaga = int(input("Digite o código da vaga: "))
    CodFuncionario = int(input("Digite o codigo do funcionário que fará a entrevista: "))
    StatusResultado = input("Digite o resultado da entrevista: ")
    dados = {"Codigo":Codigo, "DataEntrevista":DataEntrevista, "CodCandidato":CodCandidato, "CodVaga":CodVaga,
                        "CodFuncionario":CodFuncionario, "StatusResultado":StatusResultado}

    url = "http://localhost/entrevistas"
    Dados = Req.api.post(url, json=dados).json()
    print(Dados)

def deletar_entrevista():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    url = "http://localhost/entrevistas/" + str(Codigo)
    Dados = Req.api.delete(url).json()
    print(Dados)

def atualizar_entrevista():
    import requests as Req
    Codigo = int(input("Digite o código: "))
    DataEntrevista = date(input("Digite a data da entrevista: "))
    CodCandidato = int(input("Digite o código do candidato: "))
    CodVaga = int(input("Digite o código da vaga: "))
    CodFuncionario = int(input("Digite o codigo do funcionário que fará a entrevista: "))
    StatusResultado = input("Digite o resultado da entrevista: ")
    dados = {"Codigo": Codigo, "DataEntrevista": DataEntrevista, "CodCandidato": CodCandidato, "CodVaga": CodVaga,
             "CodFuncionario": CodFuncionario, "StatusResultado": StatusResultado}

    url = "http://localhost/entrevistas"
    Dados = Req.api.put(url, json=dados).json()
    print(Dados)

def menu():
    while True:
        print("Digite 1 para cadastrar entrevista")
        print("Digite 2 para deletar entrevista")
        print("Digite 3 para atualizar entrevista")
        print("Digite SAIR para sair")
        num = input("Digite sua escolha: ")
        if num == 'SAIR' or num == 'sair':
            return
        if num == '1':
            cadastrar_entrevista()
        if num == '2':
            deletar_entrevista()
        elif num == '3':
            atualizar_entrevista()
        else:
            print("Ei, por favor, escolha uma opção válida!")
menu()



