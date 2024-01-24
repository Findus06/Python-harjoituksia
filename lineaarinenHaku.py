def LinearSearch(n,l):
    for i in range(len(l)):
        if l[i] == n:
            return i
    return -1
    
#print(LinearSearch(5,[0,1,2,3,4,5,6,7,8,9,10]))

