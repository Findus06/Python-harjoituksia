import time
start_time = (time.time())

# Fibonacci [0,1,1,2,3,5,8,13,21,34]
def Fibonacci(n):
    Lista = [0,1]
    for i in range(n - 1):
        Lista.append(Lista[-1] + Lista[-2])
    return Lista[n]

L = [10,100,1000,10000]
for i in range(len(L)):
    Fibonacci(i)
    print("Aika:", time.time() - start_time)
    i + 1





 
