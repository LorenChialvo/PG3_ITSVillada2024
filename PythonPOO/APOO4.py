class calculator:
    def __init__(self):
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        
        self.suma(num1, num2)
        self.resta(num1, num2)
        self.multiplicacion(num1, num2)
        self.division(num1, num2)
    
    def suma(self, num1, num2):
        print("Suma: ", num1 + num2)
    
    def resta(self, num1, num2):
        print("Resta: ", num1 - num2)
    
    def multiplicacion(self, num1, num2):
        print("Multiplicación: ", num1 * num2)
    
    def division(self, num1, num2):
        if num2 != 0:
            print("División: ", num1 / num2)
        else:
            print("No se puede dividir por cero.")
calculator()