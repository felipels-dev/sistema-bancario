# Simulador de Caixa Eletronico

saldo = float('0.0')
print("\n**** Bem vindo ao Simulador de Caixa Eletronico: ****")
print(f"Seu Saldo atual é de R$  {saldo:.2f}\n")

print("####### Selecione a Opção:####### ")
print("1 - Saque")
print("2 - Deposito")
print("3 - Extrato")
print("4 - Sair")
print('####### Insira a opção desejada #######')
i = 1
extrato = ""

# Estrutura de repetição para para a quantidade de saques limites
while i <= 3:
    a = float(input())

    if a == 1:
        print("####### Selecionado Saque #######")

    elif a == 2:
        print("####### Selecionado Deposito #######")

    elif a == 3:
        print("####### Selecionado Extrato #######")

    elif a == 4:
        print("####### Obrigado por utilizar o Simulador de Caixa Eletronico #######")
        print("******** Sistema Encerrado ********")

    else:
        print("####### Opção invalida - Programa encerrado #######")
        break

# Quando selecionar Saque (Limitado a 3 nesse sistema)
    if a == 1:

        if saldo == 0:
            print('#### Não há valores disponiveis para saque ####')
            print(f"Seu saldo atual é de R$ {saldo:.2f}\n")
            print("####### Selecione a Opção: ####### ")
            print("1 - Saque")
            print("2 - Deposito")
            print("3 - Extrato")
            print("4 - Sair")
            print('####### Insira a opção desejada #######')

        else:
            print("Qual o valor do saque?")
            valor = float(input())
            saldo = saldo - valor

            if saldo < 0:
                print('####### Saldo Insuficiente ####### \n')
                saldo = 0

            else:
                print(f"Seu saldo atual é de R$ {saldo:.2f}")
                extrato += f"Saque: R$ {valor:.2f}\n"
                i = i + 1

            if i <= 3:
                print("\n####### Selecione a Opção: ####### ")
                print("1 - Saque")
                print("2 - Deposito")
                print("3 - Extrato")
                print("4 - Sair")
                print('####### Insira a opção desejada #######')

            else:
                print(extrato)
                print("Limite de saques diarios - Obrigado por usar o nosso banco\n")
                break

# Quando selecionar Deposito (sem limite)
    elif a == 2:
        print("Qual o valor de deposito? ")
        valor = float(input())
        saldo = valor + saldo
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print(f"Seu saldo atual é R$ {saldo:.2f} \n")
        print("####### Selecione a Opção:####### ")
        print("1 - Saque")
        print("2 - Deposito")
        print("3 - Extrato")
        print("4 - Sair")
        print('####### Insira a opção desejada #######')

# Extrato das suas transações
    elif a == 3:
        print(extrato)
        print(f"Seu Saldo atual é de R$  {saldo:.2f}")
        print('###################################\n')
        print("####### Selecione a Opção:####### ")
        print("1 - Saque")
        print("2 - Deposito")
        print("3 - Extrato")
        print("4 - Sair")
        print('####### Insira a opção desejada #######')

# Encerrar Sistema pelo usuário
    elif a == 4:
        break

# Caso não seja selecionada as opções solicitadas o programa encerra
    else:
        print("####### Opção invalida - Programa encerrado #######")
        break

