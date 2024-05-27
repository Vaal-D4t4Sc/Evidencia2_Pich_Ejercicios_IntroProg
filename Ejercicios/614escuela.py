#En una escuela, luego de tomar un determinado examen, es necesario calcular el promedio de notas (las notas van de 0 a 10) de los alumnos de un curso. Se necesita saber si el rendimiento ha sido elevado (el promedio es mayor a 8), aceptable (el promedio está comprendido entre 6 y 8) o bajo (promedio es inferior a 6). Desarrollar un algoritmo que resuelva este problema. Para tener en cuenta: las autoridades del colegio saben cuántos estudiantes del curso han rendido el examen.

num_estudiantes = int(input("Ingrese el número de estudiantes: "))

suma_calif = 0

for i in range(num_estudiantes):
    calif = float(input(f"Ingrese la calificaion del estudiante {i + 1}: "))
    suma_calif += calif


promedio = suma_calif / num_estudiantes
print ("La calificaion del aula es: ", promedio)


if promedio > 8:
    print("Rendimiento elevado. Felicitaciones.")
elif 6 <= promedio <= 8:
    print("Rendimiento aceptable. Buen trabajo.")
else:
    print("Rendimiento bajo. Debes esforzarte mas.")
