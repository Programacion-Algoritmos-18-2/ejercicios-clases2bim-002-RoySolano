from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]


# print(lista)
suman1 = 0
suman2 = 0
lista = lista[1:]
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])
for d in lista:
    # print(d)
    #suman1 = suman1 + int(d[4])    
    p = Persona(d[1], d[2], d[3], d[0], d[4],d[5])
    suman1 = suman1 + p.obtener_nota1()
    suman2 = suman2 + p.obtener_nota2()
    if (p.obtener_nota1() < 15 or p.obtener_nota2() < 15 ):
    	print(p.obtener_nombre())
resultado =  suman1 / len(lista)
resultado2 = suman2 / len(lista)
print(resultado)
print(resultado2)