#Introduction to Computer Science
#Function: soma_elementos
#Date: 18/02/2020
#Developed by: Rodrigo Bernardo Medeiros

#================================================================
#The program will receive a list with integer numbers and will
#sum all elements.
#================================================================

def soma_elementos(lista):

    sum  = 0
    for i in range(len(lista)):

        sum = sum + lista[i]

    return sum
        
