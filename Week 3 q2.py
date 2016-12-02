def prime(n,t):
    if n/2==True: #if n divisile by 2 is not true return n
        return n
        print("not a prime") # print prime 
    else:
        if n/2==False: # if n divisible by 2 and is false return n
            return n
            prime(t+1) #  adds another value with the variable's value and assigns the new value to the variable
            n/prime # n/prime
            if prime==n/2: # if prime is equal to n/2
                print("Its not a prime number")
prime(11,2)

