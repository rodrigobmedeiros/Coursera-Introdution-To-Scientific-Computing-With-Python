import math

Coef_a = int(input("Entre com o valor do coeficiente a: "))
Coef_b = int(input("Entre com o valor do coeficiente b: "))
Coef_c = int(input("Entre com o valor do coeficiente c: "))

Delta = Coef_b**2 - 4*Coef_a*Coef_c



if Delta > 0:

    x_1 = (-Coef_b + math.sqrt(Delta))/(2*Coef_a)
    x_2 = (-Coef_b - math.sqrt(Delta))/(2*Coef_a)

    if x_1 < x_2:

        print('as raízes da equação são', x_1, 'e' ,x_2)

    else:

        print('as raízes da equação são', x_2, 'e' ,x_1)

else:

    if Delta == 0:

        x_1 = -Coef_b/(2*Coef_a)
        print("a raiz desta equação é", x_1)

    else:

        print("esta equação não possui raízes reais")
