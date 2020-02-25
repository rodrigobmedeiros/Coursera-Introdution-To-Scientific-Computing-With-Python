numero = int(input('Entre com um numero inteiro: '))

RestoDivisao3 = numero%3
RestoDivisao5 = numero%5

if RestoDivisao5 == 0 and RestoDivisao3 ==0:

    print('FizzBuzz')

else:

    print(numero)
