from random import randint

#2. Least Common Multiple, Greatest Common Factor (Grade Factor 1)

def Least_Common_Mul(numbs):
    #function to calculate Least Comman Multiples 
    num1 , num2 = numbs
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    while(True):
        if((greater % num1 == 0) and (greater % num2 == 0)):
            lcm = greater
            break
        greater += 1
    return lcm



def Greatest_Comman_Fac(numbs):
    #Function to calculate Greatest Comman Factor
    num1,num2 = numbs
    if num1 > num2:
        small = num2
    else:
        small = num1
    for i in range(1, small + 1):
        if((num1 % i == 0) and (num2 % i == 0)):
            gcd = i
             
    return gcd

def num_Mul(num,end):
    #Function to calculate Multiples of the numbers
    c = num
    l = [] #list
    while c <= end:
        l.append(c)
        c += num

    return l 

    
def factor_Num(num):  
    #Fucntion to calculate Factors of th numbers
    fact_li = []
    for i in range ( 1, (num+1)):
        if num % i == 0 :
            fact_li.append(i)

    return fact_li


def main():
    # This function used to collect output from all the functions and output them 
    num1 = randint(2,31)
    num2 = randint(2,31)
    end = num1 * num2
    num_tub = (num1,num2) # tuple
   


    mul_num1 = num_Mul(num1,end)
    mul_num2 = num_Mul(num2,end)
    lcm = Least_Common_Mul(num_tub)
    gcf = Greatest_Comman_Fac(num_tub)
    fact_num1 = factor_Num(num1)
    fact_num2 = factor_Num(num2)

    num1_mul_str = ','.join(str(x) for x in mul_num1) # joing the element of list to string 
    num2_mul_str = ','.join(str(x) for x in mul_num2)
    print("Integer 1:",num1)
    print("Integer 2:",num2)
    print("The multiple of",num1 ,"are" , num1_mul_str) 
    print("The multiple of",num2 ,"are" , num2_mul_str)
    print("The lowest comman multiple is ",lcm)
    

    num1_fact_str = ','.join(str(x) for x in fact_num1)
    num2_fact_str = ','.join(str(x) for x in fact_num2)
    print("The factors of " ,num1,"are",num1_fact_str)
    print("The factors of " , num2 , "are",num2_fact_str)
    
    print("The greatest comman factor is",gcf)


if __name__ == "__main__":
    
    while True:
        main()
        
        try :
            i = input()
        except KeyboardInterrupt:
            print ("kmjihn")




        