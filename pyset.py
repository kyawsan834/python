setData = {"Apple","Orange","Avocado"}
print(type(setData))
print(setData)
tupleData = ("Apple","Orange,","Avocado")
print(type(tupleData))
print(tupleData)

print("Cherry" in setData)
setData.add("Cherry")
print(setData)
print("Cherry" in setData)
print(type(setData))