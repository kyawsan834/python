print("===============Profit Margin============")
print("Profit Margin = (net income / revenue) * 100")


userrevenue = int(input("Enter your revenue\n"));
userexpense = int(input("Enter your expenses\n"));

def calcProfitMargin(userrevenue,userexpense):
        userincome = userrevenue - userexpense;
        calculatingProfitMargin = int((userincome/userrevenue) * 100);
        return calculatingProfitMargin;
print(calcProfitMargin(userrevenue,userexpense))