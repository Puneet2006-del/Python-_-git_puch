class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")    

puneet = Employee()
puneet.language = "JavaScript"     # This is an instance attribute
print(puneet.language,puneet.salary)
puneet.getInfo()
puneet.greet()
# The instance attribute takes prefernce 



