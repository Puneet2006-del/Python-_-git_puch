class Programmer:
    Company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Puneet", 1200000,245001)  
print(p.name,p.salary,p.pin,p.Company)   

r = Programmer("Rohan", 1200000,245001)
print(r.name,r.salary,r.pin,r.Company)



