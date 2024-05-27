#Mostrar sólo los números pares desde 0 hasta el número ingresado (input). Nota: para saber si un número es par hacer i % 2 == 0)

num = int(input("Ingrese el número máximo a mostrar: "))

for i in range(num + 1):
    if i % 2 == 0:
        print("Número par: ", i)
