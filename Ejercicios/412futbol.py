# Un hincha de fútbol desea conocer la cantidad de puntos que su equipo lleva acumulados en el campeonato, 
# para ello recibe cada semana la información de la cantidad total de partidos, desde el inicio del campeonato, 
# que el equipo ha perdido, ha empatado y ha ganado. 
# Por cada partido empatado recibe un punto, 
# por cada partido ganado tres puntos y
# por los perdidos cero puntos.

print ("Puntos acumulados por tu equipo en el campeonato.")
empate = int(input ("Partidos empatados: "))
victoria = int(input ("Partidos ganados: "))
derrotas = int(input ("Partidos perdidos: "))
puntos = empate+victoria*3
print ("Tu equipo acumula ", puntos, " puntos")
if puntos>=145:
    print ("Felicidades, tu equipo lidera el campeonato")
else:
    print ("Buena suerte")
