with open("log.txt","r") as f:
     lines = f.readlines()

lineno = 1
for line in lines:

    if("Python" in line):
        print(f"Yes python is present, Line no: {lineno}") 
        break 
    lineno += 1
 
else:
     print("No Python is not present") 