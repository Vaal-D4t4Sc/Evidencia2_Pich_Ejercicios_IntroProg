#Identificar situaciones donde se utilice la estructura condicional para cada uno de estos casos:

#1. Condicional parcial (solo el if) con expresión lógica simple
#  a = 1
#  b = 2
#  if b > a:
#     print("b es mayor que a")

#2. Condicional completo (if - else) con expresión lógica simple
#RamaFalsaVerdadera.py (prestamo)

#3. Condicional parcial (solo el if) con expresión lógica compuesta (and)
#Ejemplo_ANDpy (entrada boliche)

#4. Condicional completo (if - else) con expresión lógica compuesta (or)
#Ejemplo_OR.py (dia semana)

#Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. 
#Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento del 10%. 
#Si compra más de 24 unidades, el descuento es del 15%. 
#Además posee la promoción a los jubilados. La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos)

print ("OFERTON Leche a $1000")
print ("Descuento por compra al por mayor")
leche = int(1000)
compra = int (input ("¿Cuantas leche va a comprar? "))
descuento1 = leche*0.90
descuento2 = leche*0.85
if compra >= 12 and compra <=23:
    print ("Te aplicaremos un descuento del 10%")
    print ("Total: ", compra*descuento1)
elif compra >=24:
    print ("Te aplicaremos un descuento del 15%")
    print ("Total: $", compra*descuento2)
else:
    print ("Total: $", compra*leche)

print ("Gracias por su compra")


