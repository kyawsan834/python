mytuple = (2,)

print(type(mytuple))

mytuple1 = ("Apple","Orange","Avocado")
print(type(mytuple1))
print(mytuple1)
mytuple1 = list(mytuple1)
print(type(mytuple1))
print(mytuple1)
mytuple1[1] = "cherry"
mytuple1 = tuple(mytuple1)
print(type(mytuple1))
print(mytuple1) 

mytuple2 = ("Cherry",)
mytuple1 += mytuple2
print(type(mytuple1))
print(mytuple1)