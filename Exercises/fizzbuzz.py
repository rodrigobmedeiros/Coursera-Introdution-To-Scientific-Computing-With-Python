#Function: fizzbuzz
#Created by: Rodrigo Bernardo Medeiros
#Date: 17/02/2020
#Define if a number is or not divisible by 3 and/or 5

def fizzbuzz(n):

    resto3 = n%3
    resto5 = n%5

    if resto3 ==0 and resto5 !=0:

        return "Fizz"

    if resto3 !=0 and resto5 ==0:

        return "Buzz"

    if resto3 ==0 and resto5 ==0:

        return "FizzBuzz"

    else:

        return n
