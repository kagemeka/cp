def adjacentElementsProduct(inputArray):
    mx = -(1 << 30)
    a = inputArray 
    n = len(a)
    for i in range(n - 1):
        mx = max(mx, a[i] * a[i + 1])
    return mx 
    

