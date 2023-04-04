def fibonnaci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else :
        return fibonnaci(n - 1) + fibonnaci(n - 2)
    
print(fibonnaci(4))
#called 6 times

def sumOfSquares(n):
    if n == 1:
        return 1
    else:
        return (n ** 2) + sumOfSquares(n - 1)
    
print(sumOfSquares(4))