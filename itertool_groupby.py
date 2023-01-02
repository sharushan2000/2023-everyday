import itertools

s = input()
for k , v in itertools.groupby(s):
    # print(k) gives the list of consecutive elements
    # print(v) value 
   print((k,len(list(v))),end="")


"""
    cout the consecutive character in a given string    

"""