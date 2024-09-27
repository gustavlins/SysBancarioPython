print("Bem-vindo! Selecione uma das opções a seguir para continuar.")

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=>d"""

# Variáveis iniciais
SALDO = 0
LIMITE_SAQUE = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        try:
            deposito = float(input("Digite o valor do depósito: R$ "))
            if deposito > 0:
                SALDO += deposito
                extrato += f"Depósito: R$ {deposito:.2f}\n"
                print(f"Depósito realizado com sucesso! Seu novo saldo é: R$ {SALDO:.2f}")
            else:
                print("O valor do depósito deve ser positivo.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido.")

    elif opcao == "s":
        try:
            valor_saque = float(input("Digite o valor que deseja sacar: R$ "))
            # Verificando as condições de saque
            if valor_saque <= 0:
                print("O valor do saque deve ser maior que zero.")
            elif valor_saque > SALDO:
                print("Saldo insuficiente para realizar o saque.")
            elif valor_saque > LIMITE_SAQUE:
                print(f"O valor do saque excede o limite de R$ {LIMITE_SAQUE:.2f} por operação.")
            elif numero_saque >= LIMITE_SAQUES:
                print("Você atingiu o limite de saques diários.")
            else:
                SALDO -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saque += 1
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
                print(f"Saldo atual: R$ {SALDO:.2f}")
        
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {SALDO:.2f}")
        print("=============================\n")

    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema bancário. Até a próxima!")
        break
    
    else:
        print("Operação inválida, por favor, selecione uma opção válida.")