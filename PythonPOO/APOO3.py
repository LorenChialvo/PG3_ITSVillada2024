class Triangulo():
    def findbiggest(self,side1,side2,side3):
        if side1>side2 and side1>side3:
            return print("El lado mayor es ",side1)
        elif side2>side1 and side2>side3:
            return print("El lado mayor es ",side2)
        else:
            return print("El lado mayor es ",side3)
        
    def equilateral(self,side1,side2,side3):
        if side1==side2 and side1==side3:
            return print("Es triangulo equilatero")
        else:
            return print("No es triangulo equilatero")
        
Triangulo1=Triangulo()
lado1=int(input("Ingrese el primer lado: "))
lado2=int(input("Ingrese el segundo lado: "))
lado3=int(input("Ingrese el tercer lado: "))
Triangulo1.findbiggest(lado1,lado2,lado3)
Triangulo1.equilateral(lado1,lado2,lado3)