import random #random import to import random.randrange #1
num=[1,2,3,4,5,6,7] # sequence of numbers #1
num2=[] #empty list to store the numbers  #1

for i in range(7): # for loop for the amount of elements in the array #n
    n=random.randrange(len(num)) #takes one element and add its to the next empty list #n
    num2.append(num[n]) #n
    del num[n] #deletes the elements in the old list #n
    print(num2) #n


#big o notation O(n)
