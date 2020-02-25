#Introduction to Computer Science
#Function: maior_elemento
#Date: 18/02/2020
#Developed by: Rodrigo Bernardo Medeiros

#================================================================
#The program will receive a list and will return the greatest
#number
#================================================================



def maior_elemento(lista):

    ListaOrdenada = sorted(lista)

    return ListaOrdenada[-1]
