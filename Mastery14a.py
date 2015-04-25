#C:\Python34\Lib\Fibonacci.py
def Fibonacci_Loop(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a + b
	return a
def Fibonacci_Recursion(n):
    if (n==0):
        return 0
    if (n==1):
        return 1
    return fib(n-1) + fib(n-2)
