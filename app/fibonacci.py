fib1 = 0
fib2 = 1      
#print(fib1)
#print(fib2)
n = 20       
i = 0
while i < n:
    fib_sum = fib1 + fib2 #fib_sum == x+y = 1 + (1+y)
    print('*'*10)
    

    fib1 = fib2    # fib1 == x = fib2 = 1
    fib2 = fib_sum  # fib2 == y = x + y = 1+y
    i = i+1
    if i>5:
        print(fib_sum)
    

