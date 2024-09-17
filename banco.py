menu = '''

[d] Despositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opção = input(menu)

    if opção == "d":
        print("Deposito")
        valor = float(input("Digite o valor do deposíto:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

            print("\nDeposito concluido no Valor de:", valor)
        else:
            print("\nOperação falhou, o valor é inválido")
    elif opção == "s":
        print("Saque")
        valor = float(input("Digite o valor do saque:"))

        exedeu_saldo = valor > saldo
        exedeu_limite = valor > limite
        exedeu_saques = numero_saques >= limite_saques

        if exedeu_saldo:
            print("\nVôce não tem saldo suficiente!")
        elif exedeu_limite:
            print("\nO valor limite de saque foi atingido. Seu valor limite de saque é de R$ 500.")
        elif exedeu_saques:
            print("\nO limite de saques foi atingido!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("\nOperação falhou, o valor informado não é válido!")

    elif opção == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opção == "q":
        print("Sair")
        break

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada.")