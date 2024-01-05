def principal():
    total_saldo = 0
    while True:
        print(" === Banco Itaú === ")
        print(" 1- Depositar")
        print(" 2- Sacar")
        print(" 3- Extrato")
        print(" 4- Sair")

        opcao = input(" > ")

        match opcao:
            case '1':
                total_saldo = depositar(total_saldo)
                print('Total:', total_saldo)
            case '2':
                total_saldo = sacar(total_saldo)
                print('Total:', total_saldo)
            case '3':
                extrato()
            case '4':
                print("Saindo do banco...")
                break
            case _:
                print('Opção inválida. Insira um numero da lista.')


def depositar(total_saldo):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            print(f"Foram depositados R${valor:.2f} na sua conta!\n")
            return total_saldo + valor
        else:
            print("Operação falhou! O valor informado é inválido")
    except ValueError:
        print("Por favor informe um número válido")

def sacar(total_saldo):
    QTD_LIMITE_SAQUE_DIARIO = 3
    LIMITE_SAQUE_DIARIO = 500

    if total_saldo == 0:
        print('Saldo insuficiente')
        return 0

    #Verificar se o limite diário de saques foi atingido
    if getattr(sacar, 'qtd_saques_diarios', 0) >= QTD_LIMITE_SAQUE_DIARIO:
        print('Você atingiu o limite de saques diários. Tente amanhã.')
        return total_saldo

    saque = float(input("Informe a quantidade a retirar: "))

    # Verificar se o saque não excede o limite máximo
    if saque > LIMITE_SAQUE_DIARIO:
        print('Operação falhou! O valor do saque excede o limite máximo.')
        return total_saldo

    # Atualizar o total de saques diários
    setattr(sacar, 'qtd_saques_diarios', getattr(sacar, 'qtd_saques_diarios', 0) + 1)

    # Atualizar o saldo
    novo_saldo = total_saldo - saque
    print(f"Foram retirados R${saque} da sua conta\n")

    return novo_saldo


def extrato():
    pass

principal()