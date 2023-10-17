import string

greet = "hello"
print(greet)
greet = greet.capitalize()
print(greet)

listItems = ["name1","name2","name3"]
items = ", ".join(listItems)


print(items)
print(type(items)) 

greetText = "hello, Today is greeting"

changeArr = greetText.split()
print(type(changeArr))