n_string = input('Digite um número inteiro: ')

caracteres = len(n_string)

i = 1

n_int = int(n_string)

divisor = 10

soma = 0

while i<=caracteres:

    if divisor == 10:''''''

        ResultadoDivisao = n_int//divisor
        RestoDivisao = n_int%divisor

        RestoResultadoDivisao = ResultadoDivisao%10
        
        soma = soma + RestoDivisao + RestoResultadoDivisao
        divisor = divisor*10
        
        i = i+2

    else:

        ResultadoDivisao = n_int//divisor
        RestoResultadoDivisao = ResultadoDivisao%10
        soma = soma + RestoResultadoDivisao
        i = i+1
        divisor = divisor*10


print(soma)
