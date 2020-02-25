#Function: maximo
#Created by: Rodrigo Bernardo Medeiros
#Date: 17/02/2020
#Receive 3 numbers and return the highest


def maximo(n1,n2,n3):

    if n1 <=n2:

        if n2<=n3:

            return n3

        else:

            return n2

    else:

        if n1<=n3:

            return n3

        else:

            return n1
