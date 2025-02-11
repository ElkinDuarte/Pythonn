num = float(input("Ingresa un numero : "))

if num > 0:
    print("El Numero es positivo" )
elif num < 0 :
    print("El Numero es negativo")
elif num == 0:
    print("El Numero es 0")


suma = 0

for i in range(5):
    num = float(input("Ingresa un numero : "))
    i = i + 1
    if num > 0:
        suma = suma + num

print(f"La suma de los números positivos es: {suma}")