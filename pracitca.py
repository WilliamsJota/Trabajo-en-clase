op = "S"
cont = 0
suma = 0
while op.upper()!="N":
    cont+=1
    x = int(input("Ingrese un numero:"))
    suma+=x
    op = input("Opcion[S/N]:")
    
print("El promedio es", str(suma/cont))