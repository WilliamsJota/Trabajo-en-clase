op = "S"
cp = 0
ci = 0
while op.upper()!="N":
    x = int(input("Ingrese un numero:"))
    if x%2==0:
        cp+=1
    else:
        ci+=1
    op = input("Opcion[S/N]:")
    
print("Numero de pares:", cp)
print("Numero de impares:", ci)