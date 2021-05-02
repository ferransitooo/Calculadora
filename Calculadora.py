#Calculadora de Ferran


#Importar:
import math
import time

name = input("Escribe tu nombre:")
print("Bienvenido "+name)
time.sleep(1)
ans1 = input("Deseas calcular algo? s/n:")
if ans1 == "n":
    print("Ok, adiós.")
    quit()

elif ans1 == "s":
    print("Ok, abriendo calculadora...")
    time.sleep(2)
    num1 = float(input("Introduce el primer número:"))
    op = input("Elige el método: +,-,*,/,^ o raíz cuadrada:")

if op == "raíz cuadrada":
    ans2 = math.sqrt(num1)
    print("Tu respuesta es:",ans2)
    quit()

num2 = float(input("Introduce el segundo número:"))

if op == "+":
    ans2 = num1 + num2
    print("Tu respuesta es:",ans2)

elif op == "-":
    ans2 = num1 - num2
    print("Tu respuesta es:",ans2)

elif op == "*":
    ans2 = num1 * num2
    print("Tu respuesta es:",ans2)

elif op == "/":
    ans2 = num1 / num2
    print("Tu respuesta es:",ans2)

elif op == "^":
    ans2 = math.pow(num1, num2)
    print("Tu respuesta es:",ans2)

