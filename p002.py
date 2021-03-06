def sumOfEvenFibs(sumLimit):
    """
    Assumes sumLimit is non-negative.
    Returns the sum of even terms of in the Fibonacci series.
    
    >>> sumOfEvenFibs(1000)
    798
    """
    
    fib = dict()
    fib[0] = 0
    fib[1] = 1
    i = 2
    
    while (fib[i-1] + fib[i-2]) <= sumLimit:
        fib[i] = fib[i-1] + fib[i-2]
        i = i + 1
    
    evenFibSum = 0
    for j in fib:
        if fib[j] % 2 == 0:
            evenFibSum += fib[j]
            
    return evenFibSum 
    
    
print(sumOfEvenFibs(4000000))
