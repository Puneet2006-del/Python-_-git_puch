with open("log.txt","r") as f:
     content = f.read()


if("Python" in content) :
     print("Yes python is present")  
else:
     print("No Python is not present")
  