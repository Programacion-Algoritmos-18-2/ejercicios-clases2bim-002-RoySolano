import codecs # importación del códecs para la lectura del archivo
import sys

class MiArchivo: #creación de clase
    """
    """
    
    def __init__(self): #método para inicializar variables globales
        """
        """
        self.archivo = codecs.open("data/demo_notas.csv", "r") #envío de direccion del archivo

    def obtener_informacion(self): #método para obtener los datos del archivo
        return self.archivo.readlines() 

    def cerrar_archivo(self): #método para cerrar el archivo 
        self.archivo.close()


class MiArchivoEscribir: #método para modificar el archivo si este se encuentra vacío
    """
    """
    
    def __init__(self): 
        """
        """
        self.archivo = codecs.open("data/demo2.csv", "a") 

    def agregar_informacion(self, p): #método para recibir un objeto y escribir en el archivo
        self.archivo.write("%s-%s-%d-%d\n" % (p.nombre, p.apellido,\
                p.edad, p.codigo)) 

    def cerrar_archivo(self): #método para cerrar el archivo
        self.archivo.close()
