n = int(input('Entre com um número natural: '))

continua = True
Fatorial = n

while continua:

    n = n-1

    if n>0:
        Fatorial = Fatorial*n

    else:

        if n==0:

            continua = False

        else:

            Fatorial = 1
            continua = False



print(Fatorial)
