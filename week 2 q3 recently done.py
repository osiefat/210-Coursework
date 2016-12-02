def matrices_multiplication(b, c):
    firstB=b[:4] #1
    firstC=c[:4] #1
    empty_list=[] #1
    for i in b: #n
        times=[b*c for b,c in zip(b, c)] #n
        empty_list.append(times) #n
        print(empty_list) #n

def matrices_addition(b, c):
    firstB=b[:4] #1
    firstC=c[:4] #1
    empty_list=[] #1
    for i in b: #n
        times=[b+c for b,c in zip(b, c)] #n
        empty_list.append(times) #n
        print(empty_list) #n

def matrices_subtraction(b, c):
    firstB=b[:4] #1
    firstC=c[:4] #1
    empty_list=[] #1
    for i in b: #n
        times=[b-c for b,c in zip(b, c)] #n
        empty_list.append(times) #n
        print(empty_list) #n

def function(b, c):
    a=b*c-2*(b+c)
    firstB=b[:4] #1
    firstC=c[:4] #1
    empty_list=[] #1 
    empty_list2=[] #1
    for i in b: #n
        times=[b*c-2 for b,c in zip(b, c)] #n 
        empty_list.append(times) #n
        return empty_list #n
        for i in b: #n^2
            times2=[times*b+c for b,c in zip(b, c)] #n^2
            empty_list2.append(times2) #n^2
            print(empty_list2) #n^2
    
function([3,8,4,6], [4,0,3,5])

#o(n^2) big O notation
