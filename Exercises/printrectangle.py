#Introduction to Computer Science
#Function: printrectangle
#Date: 18/02/2020
#Developed by: Rodrigo Bernardo Medeiros

#======================================================
#The program will receive two inputs, width and height,
#and have to print the rectangle with #
#======================================================

def printrectangle():

    width = int(input('digite a largura: '))
    height = int(input('digite a altura: '))

    c_width = 1
    c_height = 1

    while c_height <= height:

        while c_width <= width:

            print('#', end = '')
            c_width = c_width + 1

        print()
        c_height = c_height + 1
        c_width = 1

printrectangle()
    
