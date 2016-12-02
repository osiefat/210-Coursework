def find_value(list1, high, low, n): #4 attributes, list1=array of numbers, high and low=the two numbers to search for the intergers in the list 
    start = 0 #starting point #1
    end = n #size of array #1
    while(start < end): #0 compared to n (6), 0+(6-0)/2 = 3, third position aka middle value #n
        mid = int (start + (end - start) / 2)#gets the middle of the list #n
        if low > list1[mid] and high > list1[mid]:#it will compare each interger to the previous one #n
            start = mid +1 # checking each of the value then moving to the next one #n
        elif low < list1[mid] and high < list1[mid]: #1
            end = mid # value(s) found #1
        else: #1
            return True #1
        
    return False #1

list1 = [2,3,5,7,8,13]
n = 6 #size of array
high = 10 #the gap of numbers were looking for between those two
low = 14
print(find_value(list1,high,low,n))

#Big o notation O(n)
