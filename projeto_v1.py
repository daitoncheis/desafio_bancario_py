menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = [] 
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor_deposito = float(input("Informe o valor do depósito: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato_aux = extrato
            extrato_aux.append(f"Depósito: R$ {valor_deposito:.2f}")
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")

        else:
            print("Valor de depósito deve ser positivo.")

    elif opcao == "2":
        valor_saque = float(input("Informe o valor do saque: "))
        
        if numero_saques < LIMITE_SAQUES:

            if valor_saque <= saldo and valor_saque <= limite:
                saldo -= valor_saque
                extrato.append(f"Saque: R$ {valor_saque:.2f}")
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")

            elif valor_saque > saldo:
                print("Saldo insuficiente para realizar o saque.")

            elif valor_saque > limite:
                print(f"O valor do saque não pode ultrapassar R$ {limite:.2f}.")

        else:
            print("Número máximo de saques atingido.")

    elif opcao == "3":
        print("\n========= EXTRATO =========")

        if extrato:

            for movimento in extrato:

                print(movimento)  # Exibe cada movimentação no extrato
        else:
            print("Nenhuma movimentação realizada.")
        print("==========================")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("==========================\n")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida, selecione novamente uma opção no menu.")
