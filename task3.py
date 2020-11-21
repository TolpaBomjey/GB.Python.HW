userNum = int(input("Продолжаем колдовать. давай еще число >>>"))

sum = userNum + int(f"{userNum}{userNum}") + int(f"{userNum}{userNum}{userNum}")
print(sum)