class Persona:

    def inicializar(self, nombre):
        self.nombre=nombre

    def imprimir(self):
        print("Nombre",self.nombre)


# bloque principal

persona1=Persona()
persona1.inicializar("Marco")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Ana")
persona2.imprimir()
