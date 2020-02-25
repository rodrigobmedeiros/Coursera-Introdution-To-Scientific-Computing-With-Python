#Introduction to Computer Science
#Function: n_primos
#Date: 18/02/2020
#Developed by: Rodrigo Bernardo Medeiros

#=============================================================
#The program will receive a integer number (above or
#equal 2 and calculate de sum of all prime numbers, including
#2 and the number (if it's prime =D)
#=============================================================


def n_primos(n):

    #if n<2:
        #return 'The Program is not able to count prime numbers!'


    n_start = 2
    count_primes = 0
    isprime = False
    
    while n_start <= n:

        isprime = primetest(n_start)

        if isprime:

            count_primes = count_primes + 1
            isprime = False

        n_start = n_start + 1

    return count_primes


def primetest(n):

    i = 1
    count_div = 0

    while i<=n:

        rest = n%i

        if rest == 0:
            count_div = count_div + 1

        i = i + 1


    if count_div ==2:

        return True

    else:

        return False

            
    
    
        
        
