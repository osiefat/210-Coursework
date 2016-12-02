def inc_number(lis): # the array the list
    first_index=-1 #the first index of the sequence
    current=0 #to check if the next number is bigger in the sequence
    maximum=0 #compares to see if current is bigger than maximum and if it is it becomes current
    for n in range(len(lis)):
        if (n+1==len(lis)):#cheks if its is equal to the sequence
            if(current>maximum):# if current is bigger than maximum, maximum becomes current
                maximum=current
                first_index=n-maximum #starts at n, minuses maximum (the first index of the sequence)
                break
        elif (lis[n]<lis[n+1]): #else if the individual element is less than the next one, skip to the next one
            current+=1
        elif (current>=maximum): # else if current is more than or equal to maximum, maximum becomes current, starting at the first index of the sequence
            maximum=current
            first_index=n-current # starts at n, minuses current (first index of the sequence)
            current=0
    for n in range(first_index, first_index+maximum+1): #prints the statement
        print(lis[n])


inc_number([1,2,3,4,1,5,1,6,7])

