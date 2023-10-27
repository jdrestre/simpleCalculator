# Pedir al usuario que ingrese el primer número
num1 = float(input("Ingrese el primer número: "))

# Pedir al usuario que ingrese el segundo número
num2 = float(input("Ingrese el segundo número: "))

# Pedir al usuario que seleccione una operación matemática
print("Seleccione una operación matemática:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
operacion = int(input("Ingrese su elección (1/2/3/4): "))

# Realizar la operación matemática seleccionada
if operacion == 1:
    resultado = num1 + num2
elif operacion == 2:
    resultado = num1 - num2
elif operacion == 3:
    resultado = num1 * num2
elif operacion == 4:
    resultado = num1 / num2
else:
    print("Elección inválida")
    resultado = None

# Imprimir el resultado
if resultado is not None:
    print("El resultado es:", resultado)
