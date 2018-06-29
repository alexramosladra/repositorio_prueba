# -*- coding: utf-8 -*-
import sys;
print(sys.version)
print "\n"

while True:
     try:
         numero1 = int(input("proceda a elegir el primer digito de la operacion:\n"))
         print numero1
         break
     except (NameError , ValueError , SyntaxError):
         print("el valor introducido no es valido")

operacion = raw_input("proceda a elegir el simbolo de la operacion a realizar\n")

if operacion != "+" or operacion != "-" or operacion != "x" or operacion != "/":

    while operacion !="+" and operacion !="-" and operacion !="x" and operacion !="/" :
        print "\nel simbolo introducido no es valido solo se permiten utilizar los simbolos +,-,x o /"
        operacion = raw_input("proceda a elegir el simbolo de la operacion a realizar nuevamente \n")

if operacion == "+":
    while True:
         try:
             numero2 = int(input("proceda a elegir el segundo digito de la operacion\n"))
             print str(numero2) + "\n"
             break
         except (NameError , ValueError , SyntaxError):
             print("el valor introducido no es valido")
    suma = numero1 + numero2
    print str(numero1) + str(operacion) + str(numero2) + "=" + str(suma)

elif operacion == "-":
    while True:
         try:
             numero2 = int(input("proceda a elegir el segundo digito de la operacion\n"))
             print str(numero2) + "\n"
             break
         except (NameError , ValueError , SyntaxError):
             print("el valor introducido no es valido")
    resta = numero1 - numero2
    print str(numero1) + str(operacion) + str(numero2) + "=" + str(resta)

elif operacion == "x":
    while True:
         try:
             numero2 = int(input("proceda a elegir el segundo digito de la operacion\n"))
             print str(numero2) + "\n"
             break
         except (NameError , ValueError , SyntaxError):
             print("el valor introducido no es valido")
    multiplicacion = numero1 * numero2
    print str(numero1) + str(operacion) + str(numero2) + "=" + str(multiplicacion)

elif operacion == "/":
    while True:
         try:
             numero2 = int(input("proceda a elegir el segundo digito de la operacion\n"))
             print str(numero2) + "\n"
             break
         except (NameError , ValueError , SyntaxError):
             print("el valor introducido no es valido")
    division = numero1 / numero2
    print str(numero1) + str(operacion) + str(numero2) + "=" + str(division)

print "\n                >>> アレックスは素晴らしい <<<"
