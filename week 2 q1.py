inp=int(input("choose a number: ")) #input command
def powers(n):
    while n**2>0: # while n power 2 is bigger, move on to the next one
        n+=1
        if n==100: # exit loop 
            break
        if inp is n**2: # if n value the same as n squared return the input
            return inp
        if inp<=n**2: # if its lower than or the same then print input
            print(inp**0.5)
        elif inp>=n**2: # else if higher print input times 0.5
          print(inp**0.5)
        else:
            print("nothing") # else if it doesnt match the criteria, print nothing
powers(1)
