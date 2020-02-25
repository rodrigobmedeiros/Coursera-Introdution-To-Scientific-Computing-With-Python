#Introduction to Computer Science
#Function: inverte_sequencia
#Date: 18/02/2020
#Developed by: Rodrigo Bernardo Medeiros

#================================================================
#The program will get numbers from input and will print values in
#inverse order
#================================================================

def inverte_sequencia():

    input_list = []

    input_number = int(input('Digite um número: '))
    
    while input_number != 0:
        input_list.append(input_number)
        input_number = int(input('Digite um número: '))
        

    input_list.reverse()

    for i in range(len(input_list)):

        print(input_list[i])
