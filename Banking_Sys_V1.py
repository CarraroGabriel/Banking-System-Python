menu = """
============== MENU ==============
      
[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

===================================
    Bem vindo usuário!

=> """

saldo = 0
limite = 500
extrato = ""
num_saques = 0
lim_saques = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("\nInforme o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n" 
        else:
            print("\nOperação não pode ser concluída, o valor que desejou depositar é inválido.")

    elif opcao == 2:
        valor = float(input("\nInforme o valor que deseja sacar: "))
        if valor > saldo:
            print("\nOperação inválida, você não tem saldo suficiente!")
        elif valor > limite:
            print("\nOperação inválida, valor desejado excede o limite!")
        elif num_saques >= lim_saques:
            print("\nOperação inválida, limite de saques excedido!")
        elif valor > 0:
            saldo -= valor
            extrato += f"\nSaque: R$ {valor:.2f}\n"
            num_saques += 1
        else:
            print("\nOperação não pode ser concluída, o valor que desejou sacar é inválido.")

    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == 0:
        print("\nObrigado por utilizar nosso sistema!!")
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")