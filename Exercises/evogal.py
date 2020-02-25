#Function: evogal
#Created by: Rodrigo Bernardo Medeiros
#Date: 17/02/2020
#Receive a letter and define if it's a vowel or a consonant


def vogal(letra):

    a = 'a'
    e = 'e'
    i = 'i'
    o = 'o'
    u = 'u'
    isvowel = False

    if letra == a or letra =='A':

        isvowel = True

    if letra == e or letra =='E':

        isvowel = True

    if letra == i or letra =='I':

        isvowel = True

    if letra == o or letra =='O':

        isvowel = True

    if letra == u or letra =='U':

        isvowel = True


    return isvowel
