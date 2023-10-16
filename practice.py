print("hay")
print("hay\nhi") 

"""
name = "Kyaw San"
age = 21
weight = 77.3
isLearning = True 
isboring = False 
print(name,age,weight,isLearning,isboring) 
""" 



"""
print("Enter your name")
input("Enter your name\n") 

"""

print("==========Input=========")


age = input("Enter your age\n");
print("You are " + age ); 

username = input("Enter your name");
countUsername = len(username)
print(countUsername)

print("==========Check DataType =========")
print("========== type() =========")

print(type(username))
print(type(countUsername)) 

print("==========Data Type Convert=========")
print("Convert to String : str(), \nConvert to int : int(), \nConvert to float()")


numberInt = 1;
floatNumber = 2.1;
stringText = "hay"

convertAll = "";
print(convertAll)

convertAll = int(numberInt); 
print(convertAll)
convertAll = int(floatNumber);
print(convertAll)
convertAll = float(numberInt)
print(convertAll)
convertAll = int(floatNumber)
print(convertAll)
print(len(stringText))
convertAll = str(numberInt)
print(type(convertAll))  

print("========== Assignment Operator and Arithmathics Operator  =========")
a = 1;
a += 1;
a = a+1; 
print(a)

print(type(a))

a = 2 * 1
print(a) 
print(type(a))

a = 2 / 1
print(a)
print(type(a))

a = 2 - 1
print(a) 
print(type(a)) 

a = a ** 2
print(a)
print(type(a))

a = a // 2
print(a)
print(type(a))

a = a % 2
print(a)
print(type(a)) 

a = 1+ 2 /34*(54.5)%2+2-1;
print(a)
print(type(a)) 

b = 2

x = 30
y = 20
print(x == y)

print (x != y)

print(x > y)
print(x >= y)


print(x < y)
print(x <= y) 







print("========== F String () =========") 
number = 20;
numFloat = 12.0;
isWork = True;
userNameString = "hay"
print(f"number : {number} \n float : {numFloat} \n boolean : {isWork}  \n string : {userNameString} \n") 

print("==========Break Even Point (Challange) =========")
priceShopPerMonth = 2500
priceSellProcut = 2.95 
priceProductCost = 1.40
breakEvenPointPerMonth = round(priceShopPerMonth/(priceSellProcut-priceProductCost))
print(f"You need to sell approximately {breakEvenPointPerMonth} cups of coffee each month to break even") 

print("==========if condition =========")

condition = True

if condition:
    print("True Condition") 
else:
    print("False Condition")

hours = int(input("Enter your learning time\n"))
if hours >= 3:
    coding = int(input("Enter your coding time \n"))
    if coding>=5:
        print("You start reading ")
    else:
        print("You can code until 1PM")
elif hours >5:
    print("learn new task")
else:
    print("Still learning") 

print("========== Providing discount (Challange) =========")

quanity = int(input("Enter your product"))
cost = quanity * 50 
discountPricefor500Price = 15 
discountPricefor200Price = 5 
discountfor500Price = (cost/100) * discountPricefor500Price 
discountfor200Price = (cost/100) * discountPricefor200Price 

print("adding logical operator") 

membershipNew = "new"
membershipOld = "old"
membershipVIP = "vip"


if (cost >= 500 and membershipNew == "new") or (cost >= 500 and membershipNew == "vip") :
    print(f"Your cost : {cost}$ your discount {int(discountPricefor500Price)}%\n Your Payment ${cost-discountPricefor500Price}") 

elif (cost >= 200 or membershipOld == "old")  or (not cost >= 200 or membershipOld == "old"):

    print(f"Your cost : {cost}$ your discount {int(discountfor200Price)}%\n Your Payment ${cost-discountfor200Price}")  
else:
    print(f"Your cost {cost}") 

print("==========Logical Operator =========")
print("and")
print("or")
print("not") 

print("==========List =========")

fruits = ["Apple","Orange","Lemon","Banana","Avocado"]
print(fruits[0])
print(fruits[2])
print(fruits[-1]) 
fruits[4] = "PineApple"
print(fruits) 

print("Before insert list \n" , fruits )
print("After insert list ")
fruits.insert(1, "hay I am new list item") 
print(fruits) 

fruits.append("hello") 
print(f"Using append() method to add data {fruits}")

fruits.append("hay")
print(f"Using append() method to add data {fruits}")

fruits.extend([1,2,3,"new item1","new items added"])
print(f"Using extend() method to add data {fruits}")

fruits.extend("extend working ")
print(f"Using extend() method to add data {fruits}")

print(fruits)
print("Before delete list") 
fruits.remove("Apple")
print(f"Using remove() method to remove data {fruits}")
fruits.pop()
fruits.pop(1)
fruits.pop(2)
print(f"Using pop() method to remove data {fruits}")

fruits = ["Apple","Orange","Lemon","Banana","Avocado"]

print(fruits)

print("Finding list with count()")
print(fruits.count("Apple"))
print("Finding list index with index() index(give your value to find index)")
print(fruits.index("Apple"))
print(len(fruits)) 
print(sorted(fruits))


print(fruits)


print("=================List Method===============")
numbers = [1,2,3,4,5,6,7,8,9]
print(min(numbers))
print(max(numbers))
print(sum(numbers)) 
addNumbers = sum(numbers)
totalNumberLength = len(numbers)
averageNumber = addNumbers/totalNumberLength
print(averageNumber)

print("End Of Python Basic Advance Intermediate\nMove to Python Framework") 

print("==============Even Number (Challange)==============")
"""evenNumberList = []
num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n")) 
if (num1 % 2 == 0 and num2 % 2 == 0):
    evenNumberList.append(num1)
    evenNumberList.append(num2)
    print(evenNumberList) 
    print("even number added")
else:
    print("Error, only even number will listed ") 
    """

print("============While Loop==========") 
"""listItems = [] 
isTrue = True;
while isTrue:
    userAsk = input("Continue?")
    if userAsk == "y" : 
        number = int(input("Enter number one : \n"))  
        if (number % 2 == 0) : 
            listItems.append(number); 
    else: 
        print(sorted(listItems))
        isTrue = False
       """ 

listItems = []
countTotal = 0;
while countTotal < 3:
    req = int(input(f"{countTotal+1} : Enter a number"))
    if(req % 2 == 0):
        listItems.append(req)
    countTotal = countTotal+1 

print(sorted(listItems))     

print("================For Loop=============")
numberItems = []
nums = [1,2,3,2,44,3,4,444,44]

"""for countForLoop in range(3): 
    req2 = int(input(f"{countForLoop+1} : Enter a number"))
    if(req2 % 2 == 0):
        numberItems.append(req2)
print(numberItems)""" 

for allnuber in nums :
    if(allnuber % 2 == 0):
         numberItems.append(allnuber)
print(numberItems) 

print("============For Loop (Challange) ============")
numItems = []
numItems2 = []  

for totalnums in range(1,101):
    if(totalnums % 2 == 0):
        numItems.append(totalnums)
    else:
        numItems2.append(totalnums)
print(numItems,'\n',numItems2)  

print("======================password generator (challange)======================")
import random
import string

passwordLength = int(input("How many characters in password should be ")) 

pLower = string.ascii_lowercase
pUpper = string.ascii_uppercase
pNumber = string.digits
pSymbols = string.punctuation

pAllPassword = pLower + pUpper + pNumber + pSymbols 
generatePassword = random.sample(pAllPassword,passwordLength)

passwordGenerate = "".join(generatePassword)

print(passwordGenerate)



    


    









