# escreva o seu programa

contagem = 'sim'
contapar = 0
contaimpar = 0

while contagem != 'não':
    
    numero = int(input('Entre com um número inteiro positivo: '))
    RestoDivisao = numero%2
    
    if RestoDivisao == 0:
        
        contapar = contapar + 1
        
    else:
        
        contaimpar = contaimpar + 1
        
        
    print('Deseja entrar com mais algum número?')
    contagem = input('Escreva sim ou não: ')

    
print('numero de pares:',contapar)
print('numero de impares:',contaimpar)
