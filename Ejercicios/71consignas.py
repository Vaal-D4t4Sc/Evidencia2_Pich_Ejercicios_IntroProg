#Desarrollar en Python las siguientes consignas utilizando los recursos ya vistos (variables, input, print, if, if - else, while, for) que consideren adecuados para cada uno de estos casos:

#Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos. 

nombres = []

for i in range(10):
    nombre = input(f"Ingrese un nombre {i+1}: ")
    if nombre in nombres:
        print("Nombre repetido")
        while nombre in nombres:
            nombre = input(f"Ingrese un nombre {i+1}: ")
    nombres.append(nombre)

print("\nLos nombres ingresados son:")
for nombre in nombres:
    print(nombre)
    


#Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo

nombres.pop(2)
nombres.pop(-1)
print(nombres)

nombres.sort()
print (nombres)


#Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.

print ()
print ("Ahora empezaremos otro ejercicio.")
print ()
print ("Ingrese los siguientes datos:")

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
dni = input("Ingrese el DNI: ")
email = input("Ingrese el email: ")
nac = input("Ingrese fecha de nacimiento")

persona = {"Nombre": nombre, "Apellido": apellido, "DNI": dni, "Email": email, "Nacimiento":nac}

print()
print("Datos de la persona:")
for key, value in persona.items():
    print(f"{key}: {value}")


#En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos (nombre, apellido, dni, email, fecha de nacimiento)

print ()
familia=[]

for i in range(4):
        nombre = input(f"Ingrese nombre del familiar {i+1}: ")
        apellido = input(f"Ingrese apellido del familiar {i+1}: ")
        dni = input(f"Ingrese DNI del familiar {i+1}: ")
        email = input(f"Ingrese email del familiar {i+1}: ")
        nac = input(f"Ingrese fecha de nacimiento del familiar {i+1}: ")

persona = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Email": email,
        "Fecha de Nacimiento": nac
    }
familia.append(persona)

print()
print("**Familia**")
for i, persona in enumerate(familia, 1):
    print(f"\nDatos del familiar {i}:")
    for key, value in persona.items():
        print(f"{key}: {value}")
