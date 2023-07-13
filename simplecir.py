import sys
def nor_Gate(a,b):
    return not(a or b)
    # function to perform nor gate

def and_Gate(b,c):
    return (b and c)
    # function to perfom anf gate

def or_Gate(x,y):
    return (x or y)
    # function to perform or gate



if __name__ == "__main__":
    tringger = True # trigger to call functions
    
    while tringger:
        try:
            a = int(input("Enter 0 or 1 :"))
            b = int(input("Enter 0 or 1 :"))
            c = int(input("Enter 0 or 1 :"))
            
            if (a != 0 and a != 1 ): # checking the input for a
                raise ValueError ("Invalid value ",a ,"as a input")
                
                
            elif (b != 0 and b != 1 ): # checking the input of b
                
                raise ValueError ("Invalid value ",b ,"as a input")

            elif (c != 0 and c != 1 ): #checking the input of c
                
                raise ValueError ("Invalid value ",c ,"as a input")
            else:
                break
                

        except ValueError as expt :
            print(expt) # error handling
            print("Must enter a 0 or 1 ")
            continue 
            # continue if a error happens

    output = or_Gate(nor_Gate(a,b),and_Gate(b,c)) # calling the function
    print("A","B","C" , "Output")
    print(a , b, c , output) # output
