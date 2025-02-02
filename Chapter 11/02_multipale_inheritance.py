class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the employee in {self.company}")
        
class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")




class Programmer(Employee, Coder ):
    company = "ITC Infotech"
    def showLanguages(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.showLanguages()
b.printLanguages()