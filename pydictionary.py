userData = {
    "userOne" : {
        "username" : "allen",
         "password" : "123@allen",
         "address" : "Switzerland",
         "isOnline" : True,
        "gender" : "Male",
        "contact" : "123456789",
        "education" : ["html","css","js","python","node","postgresSQL"],
        "experience" : {
            "Frontend" : "html,css,js",
            "Backend" : "python,node",
            "FullStack" : "Python,Node,C#,PostgresSQL",
        },
    }, 
} 


print(userData)
print(type(userData))

print("============ add new item ============")
userData["userOne"]["Skills"] = "FullStack " 
print(userData )
