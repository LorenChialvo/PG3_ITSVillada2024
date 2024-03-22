class alumno():
    def name(self,name):
        self.name=name
    def grade(self,grade):
        self.grade=grade
    def print1(self):
        print(self.name)
        print(self.grade)
        if self.grade<4:
            print(self.name," esta Libre")
        else:
            print(self.name," esta Regular")

persona1=alumno()
persona1.name("Juan")
persona1.grade(5)
persona1.print1()
persona2=alumno()
persona2.name("Maria")
persona2.grade(3)
persona2.print1()