print ("*********************************")
print ("*** CONVERSION DE TEMPERATURA ***")
print ("*********************************")
Temperatura = float (input("Cual es la temperatura en grados Fahrenheit: "))
Celsius = float ((5*(Temperatura-32))/9)
print ("La temperatura en grados Celsius es: ", Celsius)
if (Celsius <100):
    print ("El agua no hierve a esta temperatura")
else:
    print ("El agua hierve a esta temperatura")
input ()
