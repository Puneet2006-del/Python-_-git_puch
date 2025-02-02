def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [ 45,5556,47,55624,72,56,23,65,779,741,56799,8]
f = list(filter(divisible5, a))
print(f)