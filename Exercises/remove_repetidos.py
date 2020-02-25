#Introduction to Computer Science
#Function: remove_repetidos
#Date: 18/02/2020
#Developed by: Rodrigo Bernardo Medeiros

#================================================================
#The program will receive a list and remove repeated elements.
#In addition, returns the list sorted in ascending order.
#================================================================


def remove_repetidos(lista):

    novalista = []
    
    
    for i in range(len(lista)):

        item_atual = lista[i]

        if novalista.count(item_atual) == 0:
            novalista.append(item_atual)


    CloneList = novalista[:]
    ListaOrdenada = sorted(CloneList)

    return ListaOrdenada
