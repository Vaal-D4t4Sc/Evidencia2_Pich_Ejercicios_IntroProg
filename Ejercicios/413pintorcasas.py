# Un pintor de casas debe hacer un presupuesto para un cliente. Lo que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. 
# El cliente le indica que necesita conocer el costo de mano de obra para pintar una pared rectangular de un galpón. 
# El pintor cobra un monto ﬁjo por cada metro cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para pintar la pared.

base = float (input ('Ingrese el ancho de la pared '))
altura = float (input ('Ingrese el alto de la pared '))
metro_costo = 430
pared = base*altura
print ('La pared tiene un area de ', pared)
print ('El costo de mano de obra será ', (pared*metro_costo))
