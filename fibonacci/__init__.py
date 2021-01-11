result = {}

def fibonacci(n):
    if n == 0: return 1
    if n == 1:
        return 1
    if n >= 2:
        if n in result :
            return result[n]
        else: 
            result[n] = fibonacci(n-1)+fibonacci(n-2)
            return result[n]



def fibonacci2(n):
    if n < 3: return n
    if n >= 3:
        if n in result:
            return result[n]
        else:
            result[n] = fibonacci2(n-1)*fibonacci2(n-2)+fibonacci2(n-3)
        return result[n]




def fibonacciimp(n):
    if n <= 1: return 1
    u0 = 1
    u1 = 1
    while n > 2:
        t= u1
        u1 = u0 + u1
        u0 = t
        n = n -1
    return u1




# v = int(input("Entre un nombre: "))

#print("fib("+str(v)+")="+str(fibonacci2(v)))
for i in range(10):
    print("fib("+str(i)+")="+str(fibonacci2(i)))
