# Todos los algoritmos se deben presentar en un unico programa con un menú. El progrma debe terminarse cuando el usuario elija la opción 99.
i=0
while i == 0:
    print("Bienvenido a la Miscelanea")
    print("1- Calcular el area de un triangulo  \n2- Sumar dos valores  \n3- Elevar numero al cuadrado  \n4- Conversor de moneda Euros a Dolares  \n5- Area y perimetro de un cuadrado  \n6- Area y Volumen de un cilindro  \n7- Longitud y área de un circulo  \n8- promedio de tres numeros ")
    menu=int(input("Seleccione el numero de la funcion que desea realizar \n"))

    if (menu == 1 ):
        print("1- Calcular el area de un triangulo")
        num1=float(input("Dijite la base\n"))
        num2=float(input("Dijite la altura\n"))

        resul= (float(num1 * num2)/2);

        print( f"El area de el triangulo es {resul :.2f}") 
        
    elif(menu == 2):
        print("2- Sumar dos valores")
        num1=float(input("Dijite su primer numero \n"))
        num2=float(input("Dijite su segundo numero \n"))
        resul =(float(num1+num2))
        print(f"El resultado de la suma es {resul :.2f}" )

    elif(menu == 3):
        print("3- Elevar numero al cuadrado")
        num1= float(input("Dijite la base  \n"))
        num2= float(input("Dijite la exponente  \n"))
        print("El resultado es:")
        print(pow(num1,num2))
        #resul=float(num1*num1)
        #print(f"El resultado es {resul :.2f}" )
    elif(menu == 4):
        print("4- Conversor de moneda Euros  a Dolares")
        dolar= 1.08
        num1=float(input("Dijite cuantos euros va a converitr \n"))
        resul =(float(dolar * num1))
        print(f"El valor del dolar actual mente es de 1.08 el resultado es {resul :.4f} €")
    elif(menu == 5):
        num1 = float(input("Digite el Valor de un lado"))
        area= num1 * num1
        perimetro = num1 * 4
        print(f"El area del cuadrado es {area :.2f} \n  "+f"\nEl perimetro del cuadrado {perimetro :.2f} \n")

    elif(menu == 6):
        print("6- Area y Volumen de un cilindro")
        num1=float(input("Digitel el radio del cilindro \n"))
        num2=float(input("Digitel la altura del cilindro \n"))
        areaBase= float(3.1416* (num1*num1))
        vol = float (areaBase * num2)
        print(f"La area del cilindro es {areaBase :.2f} "  + f"\nEl volumen del cilindro es {vol :.2f} \n ")

    elif(menu == 7):
        print("7- Longitud y área de un circulo")
        num1=float(input("Digite el radio del circulo "))
        long= float(2 * 3.1416 * num1)
        areaBase= float(3.1416* (num1*num1))
        print(f"La area del circulo es {areaBase :.2f}\n" + f"La longitud del circulo es {long :.2f} \n " )

    elif(menu == 8):
        print("8- promedio de tres numeros ")
        num1=float(input("Digite el primer numero \n"))
        num2=float(input("Digite el segundo numero \n"))
        num3=float(input("Digite el tecer numero \n"))
        resul=float((num1 + num2 + num3)/3)
        print(f"El promedio es {resul :.2f} ")

    else:
        print("DIGITE UN OPCION VALIDA")

    
    valor=str(input(" \nDesea utilizar otra funcion SI (S) o NO (N))? \n"))
    
    if (valor == "N" or valor == "n"):
       print ("GRACIAS POR UTILIZAR LA MISCELANEA")
       break

   


