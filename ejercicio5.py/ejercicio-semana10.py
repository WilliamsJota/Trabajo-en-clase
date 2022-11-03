cadena1 = "Hola mundo"
cadena2 = "tu puedes conquistarlo"
print(cadena1,cadena2)
print(len(cadena1))
#ejemplos2
cad = input("Ingrese nombre: ")
if len(cad)>=8:
    print(cad)
else: 
    print("Ingresar cadena mayor a 8 caracteres")
    
op = "S"

while op.upper()!="N":
    cad = input("Ingresar nombre: ")
    if len(cad)>=8:
        print(cad)
    
    else:
        print("Ingresar cadena mayor a 8 caracteres")
    op = input("Para terminar el programa introduzca [N] y  para seguir introduzca [S]")