# Example :
# Input: num1 = "11", num2 = "123"
# Output: "134"


def addStrings(num1: str, num2: str) -> str:
    if num1 == "": return num2
    if num2 == "": return num1

    sum=int(num1[-1])+int(num2[-1])
    if sum >= 10: # if sum>=10, the carry will be an argument for a nested recursive call
        return addStrings(addStrings(num1[:-1], num2[:-1]), "1") + str(sum - 10)
    #elif sm < 10:
    return addStrings(num1[:-1],num2[:-1])+str(sum)


num1 = "11"
num2 = "123"
print(addStrings(num1, num2))
