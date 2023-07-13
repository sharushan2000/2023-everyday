def norgate(a,b):
    return (not (a or b))

def andgate(a,b):
    return (a and b)

def orgate(x,y):
    return (x or y)



if __name__ == "__main__":
    cond  = True

    while cond:

        try :
            a = int(input())
            b = int(input())
            c = int(input())
            if (a == 1 or a == 0 ) and  (b == 1 or b == 0 ) and  (c == 1 or c == 0 ):
                cond = False
            else:
                raise  ValueError ('invalid a value',"cannot enter", a,b,c, "as  an input.")
        

        except ValueError as excpt:
            print (excpt)
            print("Must enter 1 or 0 as a input")

            
    output = orgate(norgate(a,b),andgate (b,c))
    print(output)
