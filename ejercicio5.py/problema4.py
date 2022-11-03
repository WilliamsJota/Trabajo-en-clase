from math import sqrt
catO = int(input("Ingrese el primer cateto:"))
catA = int(input("Ingrese el segundo cateto:"))

H = sqrt(pow(catO,2)+pow(catA,2))

print("La hipotenusa vale: ", H)