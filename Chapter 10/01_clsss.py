class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

puneet = Employee()
puneet.name = "Puneet"     # This is an instance attribute
print(puneet.language,puneet.salary,puneet.name)

rohan = Employee()
rohan.name= "Rohan"
print(rohan.salary,rohan.language,rohan.name)



# Here name is instance attribute and salary and language are class attributes as they directly belong to the class


