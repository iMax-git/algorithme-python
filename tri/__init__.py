import random
table  = [random.randint(0,20) for i in range(20)]
print(table)

def triSelection(table):
    for i in range(len(table)-1):
        minIndex = i
        minValue = table[i]
        for j in range(i+1,len(table)):
            if(table[j]<minValue):
                minValue = table[j]
                minIndex = j
        table[minIndex] = table[i]
        table[i] = minValue
        
triSelection(table)
print(table)

def  indexOf(table,value):
    i = 0
    for nbr in table:
        if nbr == value:
            return i
        i += 1 
    return -1
print(indexOf(table, 10))



def rechercheDichotomie(table,value):
    first = 0 
    last = len(table)-1
    while first <= last:
        middle  = (first+last)//2
        if(table[middle] == value):
            return middle
        if(table[middle] < value):
            first = middle +1
        if(table[middle] > value):
            last = middle -1
    return -1

print(rechercheDichotomie(table, 8))


def rechercheDichotomieRecursive(table,value):
    return rDr(table, value, 0, len(table)-1)


def rDr(table,value,first,last):
    if(first > last):
        return -1
    middle  = (first+last)//2
    if(table[middle] == value):
            return middle
    if(table[middle] < value):
        return  rDr(table, value, middle+1, last)
    if(table[middle] > value):
        return  rDr(table, value, first, middle-1)
         
print(rechercheDichotomie(table, 8))

def triFusion(table):
    first = 0
    last = len(table)-1
    return division(table,first,last)
    
def division(table,first,last):
    if(last == first):
        return [table[first]]
    middle = (first+last)//2
    t1 = division(table, first, middle)
    t2 = division(table, middle+1,last)
    return fusion(t1,t2)

def fusion(t1,t2):
    n =len(t1)+len(t2)
    result = [0] * n
    i1 = 0
    i2 = 0
    i = 0
    while(i<len(t1)+len(t2)):
        if(i1 == len(t1)):
            result[i] = t2[i2]
            i2 += 1
            i += 1
        elif(i2 == len(t2)):
            result[i] = t1[i1]
            i1 += 1
            i += 1
        elif(t1[i1]<t2[i2]):
            result[i] = t1[i1]
            i1 += 1
            i += 1
        else:
            result[i] = t2[i2]
            i2 += 1
            i += 1
    return result
        
    
triFusion(table)
print(table)
    

