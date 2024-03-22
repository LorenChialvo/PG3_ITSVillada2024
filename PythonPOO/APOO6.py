class family():
    def __init__(self):
        self.fathername = ""
        self.mothername = ""
        self.children_list = []
    def F_names(self):
        self.fathername = str(input("Ingrese el nombre del padre: "))
        self.mothername = str(input("Ingrese el nombre de la madre: "))
        print("Introduzca una lista con el nombre de los hijos, o presione ENTER para finalizar")
        while True:
            child = str(input(">> "))
            if child == "":
                break
            self.children_list.append(child)
    def __str__(self):
        children_str = ", ".join(self.children_list)
        return "El nombre del padre es: " + self.fathername + "\nEl nombre de la madre es: " + self.mothername + "\nLos nombres de los hijos son: " + children_str    
Familia1 = family()
Familia1.F_names()
print(Familia1)
