class Car:
    wheels = 4
    color = "red"
    model = "Tesla"
    carType = "charging type"
    ischargingType = True

    def carStart():
        print("Car start")
        print(f"Car is {Car.model} and is {Car.carType} ")


Car.carStart()


class UserForm:
    def __init__(self, username, email, address, contact):
        self.name = username
        self.userEmail = email
        self.userAddress = address
        self.userContact = contact

    def __str__(self):
        return (f"hello {self.name} ")

    def greeting(self):
        print(f" You are using {Car.carType}")


newUser = UserForm("user", "user@email.com", "UK", 1234)
newUser2 = UserForm("user2", "user2@email.com", "UK", 1234)

print(newUser)
print(newUser.name)
print(newUser.userEmail)
print(newUser.userAddress)
print(newUser.userContact)
