class person():
    def defined(self,name):
        self.name=name
    def print1(self):
        print(self.name)

persona1=person()
persona1.defined("Juan Martin")
persona1.print1()
persona2=person()
persona2.defined("Maria")
persona2.print1()