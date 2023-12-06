from es_bisiesto import*
print("comprobar si un ano es bisiesto:")
ano=int(input("teclea un ano:"))
while ano>=0:
    if esbisiesto(ano)==True:
        print("es bisiesto")
        ano=int(input("teclea un ano:"))    
    if esbisiesto(ano)==False:
        print("no es bisiesto")
        ano=int(input("teclea un ano:"))