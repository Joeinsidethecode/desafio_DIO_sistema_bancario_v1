cliente = input('Informe seu nome:')
print(f'----------------------------------------------------------------------')
print(f'Olá {cliente.upper()}! O Banco Itander-Bradescaixa lhe dá as boas-vindas.') 
print(f'----------------------------------------------------------------------')
menu = f'''
Qual operação deseja realizar hoje?
[1] Depósito
[2] Saque
[3] Extrato
[4] Encerrar
----------------------------------------------------------------------
=>
'''
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ''
while True:
    opcao = input(menu)
    if opcao == '1':
        valor = float(input('Valor do depósito: R$'))
        if valor > 0:
            saldo  += valor
            extrato += f'Depósito:  R$ {valor:.2f}\n'
        else:
            print('Valor inválido. Informe corretamente o valor.')
        print(f'Deposito: R$ {valor:13.2f} \nSaldo atual: R$ {saldo:10.2f}')    
    
    elif opcao == '2':
        saque = float(input('Valor do saque: R$')) 
        if saque > saldo and saque > 0:
            print(f'Saldo atual: R$ {saldo:.2f} \nSeu saldo é insuficiente. A operação não foi realizada.')
        elif saque <= saldo:
            if saque > limite:
                print(f'Seu valor de saque excede seu limite de R$ {limite:.2f} diários. A operação não foi realizada. \nSaldo atualizado: R$ {saldo:.2f}')
            elif numero_saques >= LIMITE_SAQUES:
                print(f'Seu limite de {LIMITE_SAQUES} saques diários foi excedido. A operação não foi realizada. \nSaldo atualizado: R$ {saldo:.2f}')
            else:
                saldo -= saque
                extrato += f'\nSaque:     R$ {saque:.2f}\n'
                numero_saques += 1 
                print(f'Saque realizado com sucesso. \nSaldo atualizado: R$ {saldo:.2f} ')       
                
    elif opcao == '3':
        print('========================================================')
        print('                      EXTRATO')
        print('========================================================')
        print(f'{extrato}\nSaldo:     R$ {saldo:.2f}')
        print('========================================================')

    elif opcao == '4':
        print('---------------------------------------------------------------------')
        print(f'Obrigado por utilizar nossos serviços, {cliente.upper()}. Tenha um ótimo dia!')
        print('---------------------------------------------------------------------')
        break
    else:
        print('Valor inválido. Selecione novamente a operação desejada.')
        
        
        
        
        
        
        
        
        
        
        
    