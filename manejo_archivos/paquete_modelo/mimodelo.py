"""
    creación de clases
"""

class Persona(object):
    """
    """
    
    def __init__(self, n, ape, ed, cod,n1,n2):
        """
        """
        self.nombre = n
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota1 = int(n1)
        self.nota2 = int(n2)

    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad
    
    def agregar_codigo(self, n):
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self):
        """
        """
        return self.codigo
    
    def obtener_apellido(self):
        """
        """
        return self.apellido

    def agregar_nota1(self,n):
        self.nota1 = n

    def obtener_nota1(self):
        return self.nota1

    def agregar_nota2(self,n):
        self.nota2 = n

    def obtener_nota2(self):
        return self.nota2

    
    def __str__(self):
        """
        """
        return "%s - %s - %d - %d - %d - %d" % (self.nombre, self.apellido,\
                self.edad, self.codigo, self.nota1, self.nota2)


class OperacionesPersona(object):
    """
    """
    
    def __init__(self, listado):
        """
        """
        self.listado_personas = listado
        


    def obtener_promedio_1(self):
        suma = 0
        for n in self.listado_personas:
            suma = suma + n.obtener_nota1()
        promedio_1 = suma / len(self.listado_personas)
        return promedio_1

    def obtener_promedio_2(self):
        suma = 0
        for n in self.listado_personas:
            suma = suma + n.obtener_nota2()
        promedio_2 = suma / len(self.listado_personas)
        return promedio_2

    def obtener_listado_n1(self):#método para extraer las personas con las primeras notas menores a 15
        cadena = ""
        for n in self.listado_personas:
            if (n.obtener_nota1() < 15):
                cadena = "%s\n%s %s\n" % (cadena, n.obtener_nombre(), n.obtener_apellido())

        return cadena

    def obtener_listado_n2(self):#método para extraer las personas con las segundas notas menores a 15
        cadena = ""
        for n in self.listado_personas:
            if (n.obtener_nota2() < 15):
                cadena = "%s\n%s %s\n " % (cadena, n.obtener_nombre(), n.obtener_apellido())

        return cadena

    def obtener_listado_personas(self, a , b):#método para extraer los nombres de personas con iniciales "R" o "J"
        cadena = ""
        
        for n in self.listado_personas:
            if (a == n.obtener_nombre()[0] or b == n.obtener_nombre()[0]):
                cadena = "%s\n%s %s\n " % (cadena, n.obtener_nombre(), n.obtener_apellido())
        return cadena



    def __str__(self):
        """
        """
        cadena = ""
        for n in self.listado_personas:
            cadena = "%s\n%s %s" %(cadena, n.obtener_nombre(), n.obtener_apellido())

        return cadena



