#Calculadora de Ferran
import math
num1 = float(input("Escribe el primer número:"))
meth = input("Escribe el método: +,-,*,/,^ o raíz cuadrada:")
if (meth == "raíz cuadrada"):
    ans = (math.sqrt(num1))
    print("La respuesta es:",ans)
    quit()
num2 = float(input("Escribe el segundo número:"))
if (meth == "+"):
    ans = num1+num2
elif (meth == "-"):
    ans = num1-num2
elif (meth == "*"):
    ans = num1*num2
elif (meth == "/"):
    ans = num1/num2
elif (meth == "^"):
    ans = (math.pow(num1,num2))
print("La respuesta es:",ans)










