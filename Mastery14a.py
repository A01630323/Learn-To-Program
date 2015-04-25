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
    return Fibonacci_Recursion(n-1) + Fibonacci_Recursion(n-2)
