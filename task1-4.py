userNum = input("теперь только целое положительное число >>>")
start = 0
maxNum = 0
while (start < len(userNum)):
    if (int(userNum[start]) > maxNum): maxNum = int(userNum[start])
    start += 1

print(maxNum)
