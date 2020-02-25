n = int(input('Digite o valor de n: '))

i = 1
n_natural = 1

while i<=n:

    RestoDivisao = n_natural%2

    if RestoDivisao !=0:
        print(n_natural)
        i = i + 1

    n_natural = n_natural + 1

        
    
