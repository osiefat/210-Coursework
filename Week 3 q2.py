def prime(n,t):
    if n % t ==0: #checks the remainder to see if its equal to 0
        return("not a prime") # returns prime 
    elif t==n//2: #checks if division is a whole number 
        return("A prime")
    else:
        return prime(n, t+1)
    
prime(11,2)

