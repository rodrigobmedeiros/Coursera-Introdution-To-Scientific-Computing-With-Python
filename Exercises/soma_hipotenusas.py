#Introduction to Computer Science
#Function: soma_hipotenusas
#Date: 18/02/2020
#Developed by: Rodrigo Bernardo Medeiros

#================================================================
#The program will receive a positive integer number and returns
#the sum of all integers that are hypotenuse from 1 to this num-
#ber.
#================================================================


def soma_hipotenusas(n):

    ishypotenuse = False
    i = 1
    sum_hypotenuses = 0
    
    while i<=n:

        ishypotenuse = hypotenusetest(i)

        if ishypotenuse:

            sum_hypotenuses = sum_hypotenuses + i
            ishypotenuse = False

        i = i + 1

    return sum_hypotenuses


def hypotenusetest(n):

    i = 1
    j = 1
    
    while i<=n:
        while j<=n:

            if (n**2) == (i**2 + j**2):

                return True
            
            j = j + 1
        j = 1
        i = i + 1

    return False
