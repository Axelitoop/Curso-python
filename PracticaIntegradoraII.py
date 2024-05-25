n = int(input("ingrese un numero: "))
if (n > 0):
    frase = input("Ingrese una frase: ")
    L = int(len(frase))
    factorial = int
    factorial = 1
    for i in range (1,L):
        factorial *= i+1
    if (factorial % 2 == 0):
        print("La cantidad de caracteres ingresados es de:" , L , "su factorial es de:" , factorial , "y es un numero par")
    else:
        print("La cantidad de caracteres ingresados es de:" , L , "su factorial es de:" , factorial , "y es un numero impar")