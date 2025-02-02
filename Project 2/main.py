import random 
n = random.randint(1,100)
a = -1
gusses = 1
while(a!=n):
    a = int(input("Guess The Number:"))
    if (a>n):
        print("Lower Number Please !")
        gusses +=1

    elif(a<n):
        print("Higher Number Please !")
        gusses +=1

print(f"You have gussed the number {n} correctly in {gusses} attempts\nThank You !")        



