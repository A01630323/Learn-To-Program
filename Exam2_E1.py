import math
def distancia (x1,y1,x2,y2):
	return math.sqrt((y2-y1)**2 + (x2-x1)**2)
ValorX1=int(input("Coloca el valor para x1: "))
ValorY1=int(input("Coloca el valor para y1: "))
ValorX2=int(input("Coloca el valor para x2: "))
ValorY2=int(input("Coloca el valor para y2: "))
print (distancia(ValorX1,ValorY1,ValorX2,ValorY2))
