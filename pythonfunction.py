print("=========== phtyon function ==========")  

def funOne():
    print("This is funone python") 
funOne()

def funTwobyParameter(a,b):
    print(a)
    print(b)
    print(a+b) 

funTwobyParameter(10,2) 

marks1 = [15,10,5,12,10]
marks2 = [11,10,5,12,10]

def marksAvg(arrList):
    markAvg = sum(arrList)/len(arrList)
    print(round(markAvg,2))
    
print(marksAvg(marks1))
"""
Showing none 
return the output it will fix
"""  



def marksAvg2(arrList2):
    markAvg2 = sum(arrList2)/len(arrList2)
    return round(markAvg2,2)
    
print(marksAvg2(marks1))