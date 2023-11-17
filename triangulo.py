class Triangulo:
    def inicializar(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir(self):
        print("El lado 1 es:", self.lado1)
        print("El lado 2 es:", self.lado2)
        print("El lado 3 es:", self.lado3)

    def equilatero(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("El triángulo es equilátero")
        else:
            print("No es equilátero")

    def lado_mayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("El lado mayor es 1:", self.lado1)
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print("El lado mayor es 2:", self.lado2)
        else:
            print("El lado mayor es 3:", self.lado3)

# Bloque principal

triangulo = Triangulo()
triangulo.inicializar(9, 9, 9)
triangulo.imprimir()
triangulo.equilatero()
triangulo.lado_mayor()
    
    



