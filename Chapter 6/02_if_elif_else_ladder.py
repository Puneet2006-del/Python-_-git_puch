a = int(input("Enter your age: "))

# if elif else ladder

if(a>=18):
    print("You are above the age of consent")
    print("You can drive if you have driving licence ! ")

elif(a<0):
    print("You are entering an invalid negative age ") 

 
elif(a==0):
    print("You are entering 0 which is not valid age  ")       

else:
    print("You are below the age of consent") 
    print("You cannot drive or ride kid go and cry !")   

print("End of program")
