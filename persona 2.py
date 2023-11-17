class Persona:
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

    def mayor_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")

# Bloque principal

persona = Persona()
persona.inicializar("Luis", 20)
persona.imprimir()
persona.mayor_edad()
        
