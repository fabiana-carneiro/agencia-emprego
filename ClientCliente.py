def cadastrar_cliente():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    NomeFantasia = input("Digite o nome: ")
    RazaoSocial = input("Digite a Razão Social: ")
    Segmento = input("Digite o segmento da empresa: ")
    Cnpj = input("Digite o CNPJ: ")
    Telefone = input("Digite o telefone")
    CodEndereco = int(input("Digite o Código do Endereço da empresa: "))

    dados = {"Codigo":Codigo, "NomeFantasia":NomeFantasia, "RazaoSocial":RazaoSocial, "Segmento":Segmento,
                     "Cnpj":Cnpj, "Telefone":Telefone, "CodEndereco":CodEndereco}

    url = "http://localhost/clientes"
    Dados = Req.api.post(url, json=dados).json()
    print(Dados)

def deletar_cliente():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    url = "http://localhost/clientes/" + str(Codigo)
    Dados = Req.api.delete(url).json()
    print(Dados)

def atualizar_cliente():
    import requests as Req

    Codigo = int(input("Digite o código: "))
    NomeFantasia = input("Digite o nome: ")
    RazaoSocial = input("Digite a Razão Social: ")
    Segmento = input("Digite o segmento da empresa: ")
    Cnpj = input("Digite o CNPJ: ")
    Telefone = input("Digite o telefone")
    CodEndereco = int(input("Digite o Código do Endereço da empresa: "))
    dados = {"Codigo":Codigo, "NomeFantasia":NomeFantasia, "RazaoSocial":RazaoSocial, "Segmento":Segmento,
                     "Cnpj":Cnpj, "Telefone":Telefone, "CodEndereco":CodEndereco}

    url = "http://localhost/clientes"
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
            cadastrar_cliente()
        if num == '2':
            deletar_cliente()
        elif num == '3':
            atualizar_cliente()
        else:
            print("Ei, por favor, escolha uma opção válida!")

menu()