import math

""" def squares(a, b):
    # Write your code here
    c = 0
    for i in range (a,b+1):
        if (math.isqrt(i) ** 2 == i):
            print(i)
            c += 1
            
    return c
             """
def squares2(a,b):
    c = 0 
    for i in range (a , b+1):
        x = math.sqrt(i)
        if x.is_integer():
            c += 1
    return c



if __name__ == "__main__":
    print(squares2 (3,9))