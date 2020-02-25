def fatorial(n):

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



    return Fatorial



def CoefBinario(n,k):

    if k > n:

        print('k > n, o calculo nao pode ser efetuado!')

    else:

        CoefBinario = fatorial(n)/(fatorial(k)*fatorial(n-k))
        return CoefBinario
        
