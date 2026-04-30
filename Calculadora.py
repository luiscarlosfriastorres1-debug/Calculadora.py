print("-------------Calculadora de prueba-----------")


num1 = float(input("Digite el primer numero > "))
operador = input("Operador >  ")
num2 = float(input("Digite el segundo numero"))

if operador == "+":
    total = num1 + num2
elif operador == "-":
    total = num1 - num2
elif operador == "/":
    total = num1 / num2
elif operador == "*":
    total = num1 * num2
else:
    print("No existe este operador")
    
print("El resultado es ",total)