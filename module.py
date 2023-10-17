import random

import variable

listItems = [1,2,4,3,4,4,3,2,1,2]
print(listItems)

print(random.randint(1, 19))
print(listItems)
print("================ After random ==========") 
random.shuffle(listItems)
random.choice(listItems)
print(variable.name)
print(listItems)