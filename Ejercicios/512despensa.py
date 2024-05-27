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
    total = compra*descuento1
    print ("Total: ", total)
    

elif compra >=24:
    print ("Te aplicaremos un descuento del 15%")
    total = compra*descuento2
    print ("Total: $", total)

else:
    total = compra*leche
    print ("Total: $", total)

jubilado = int(input("¿Es jubilado? Ingrese 1 de corresponder "))

if jubilado ==1:
    descuentojubilado = total*0.90
    print ("Debe abonar ", descuentojubilado)
else:
    print ("Debe abonar ", total)
     
print ("Gracias por su compra")
