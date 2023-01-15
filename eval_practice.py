# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = input().split()
p = input()

formula = p.replace('x' , x)
ans = int((eval(formula)))

if ans == int(k):
    print(True)
else:
    print(False)