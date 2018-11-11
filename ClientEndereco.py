def cadastrar_endereco():
    import requests as Req
        
    Codigo = int(input("Digite o código: "))
    Logradouro = input("Digite o logradouro: ")
    Numero = input("Digite o Numero: ")
    Cep = input("Digite o CEP: ")
    CodCidade = input("Digite o Código da Cidade: ")
    dados = {"Codigo":Codigo, "Logradouro":Logradouro, "Numero":Numero, "Cep":Cep, "CodCidade":CodCidade}
    
    url = "http://localhost/enderecos"
    Dados = Req.api.post(url, json=dados).json()
    print(Dados)

def deletar_endereco():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    url = "http://localhost/enderecos/" + str(Codigo)
    Dados = Req.api.delete(url).json()
    print(Dados)

def atualizar_endereco():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    Logradouro = input("Digite o logradouro: ")
    Numero = input("Digite o Numero: ")
    Cep = input("Digite o CEP: ")
    CodCidade = input("Digite o Código da Cidade: ")
    dados = {"Codigo": Codigo, "Logradouro": Logradouro, "Numero": Numero, "Cep": Cep, "CodCidade": CodCidade}

    url = "http://localhost/enderecos"
    Dados = Req.api.put(url, json=dados).json()
    print(Dados)

def menu():
    while True:
        print("Digite 1 para cadastrar endereço")
        print("Digite 2 para deletar endereço")
        print("Digite 3 para atualizar endereço")
        print("Digite SAIR para sair")
        num = input("Digite sua escolha: ")
        if num == 'SAIR' or num == 'sair':
            return
        if num == '1':
            cadastrar_endereco()
        if num == '2':
            deletar_endereco()
        elif num == '3':
            atualizar_endereco()
        else:
            print("Ei, por favor, escolha uma opção válida!")
menu()