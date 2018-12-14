from paquete_archivos.miarchivo import MiArchivo  #importacion de los paquetes donde estan las clases a utilizar
from paquete_modelo.mimodelo import Persona , OperacionesPersona

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]


# print(lista)

lista = lista[1:]
lista_personas = []
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])
for d in lista:
    # print(d)
    #suman1 = suman1 + int(d[4])    
    p = Persona(d[1], d[2], d[3], d[0], d[4],d[5]) # inicializamos el objeto p con  el objeto persona y le mandamos los valores de lista en tal posicion 
    lista_personas.append(p)
    
    
operaciones = OperacionesPersona(lista_personas)

print(operaciones)#presentación de información

print("Promedio 1:")#encabezado
print(operaciones.obtener_promedio_1())#presentación de información

print("Promedio 2:")#encabezado
print(operaciones.obtener_promedio_2())#presentación de información

print("Listado de notas 1:")#encabezado
print(operaciones.obtener_listado_n1())#presentación de información

print("Listado de notas 2:")#encabezado
print(operaciones.obtener_listado_n2())#presentación de información

print("Listado de nombres con iniciales R o J")#encabezado
print(operaciones.obtener_listado_personas("R", "J"))#presentación de información