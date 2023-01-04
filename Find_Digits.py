def findDigits(n):
    # Write your code here
    c = 0
    n_str = str (n)
    for i in n_str :
        if int(i) != 0:
            if n % int(i) == 0 :
                c += 1
                
    return c
                
            
        
    
    

if __name__ == '__main__':
  
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        print(result)