def revs(a):
    if a=="This is awesome": #1 # the string input
        a.split() #1 # a = split each word up 
        sen=" ".join(a.split()[::-1]) #1 # join and split the input 
        print(sen) #1 
    else: #1
        print(a) #1
revs("This is awesome") #1

# O(1) big o notation 
