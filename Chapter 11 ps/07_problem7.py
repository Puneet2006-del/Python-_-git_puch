class Vector:
    def __init__(self, l):
        self.l = l 



    def __len__(self):
        return len(self.l)
    
# Text the impementation 
v1 = Vector([1,2,3])
print(len(v1))  
        