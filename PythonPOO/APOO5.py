class persona():
    def responsabilidades(self):
        name = str(input("Ingrese el nombre de la persona: "))
        age = int(input("Ingrese la edad de la persona: "))

        self.name(name)
        self.age(age)
        

    def name(self, name):
        print("El nombre de la persona es: ", name)
    
    def age(self, age):
        print("La edad de la persona es: ", age)

class empleado(persona):
    def responsabilidades(self):
        super().responsabilidades()
        salary = int(input("Ingrese el salario de la persona: "))

        self.salary(salary)

    def salary(self, salary):
        print("El salario de la persona es: ", salary)
        if salary >= 3000:
            print("La persona debe pagar un impuesto agregado")
        else:
            print("La persona no debe pagar un impuesto agregado")
print("EMPLEADO")
Persona1= empleado()
Persona1.responsabilidades()
print("PERSONA")
Persona2= persona()
Persona2.responsabilidades()