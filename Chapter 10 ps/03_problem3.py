class Demo:
    a = 4


o = Demo()
print(o.a) # Prints the class attribute beacuse instance attribut is not present 

o.a = 0 # Instance attribute is set

print(o.a) # Prints the intance attribute beacuse instance attribute is present
print(Demo.a) # Print the class attribute 

# so its not change.
