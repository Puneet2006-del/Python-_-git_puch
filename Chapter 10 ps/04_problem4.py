class Calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The Sqaure is {self.n*self.n}")  


    def cube(self):
        print(f"The Cube is {self.n*self.n*self.n}")      

    def squareroot(self):
        print(f"The Sqaureroot is {self.n**1/2}")      



    @staticmethod
    def hello ():
        print("Hello There !")



a = Calculator(15)
a.hello()
a.square()   
a.cube()
a.squareroot()