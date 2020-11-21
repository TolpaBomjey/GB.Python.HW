print("А теперь пошли побегаем. Ну например от соседской собаки")
firstDayResult = int(input("Сколько делаем в первый день? >>>"))
goal = int(input("А сколько мы вообще планируем бежать км? >>>"))

distance = firstDayResult
day = 1
while (distance < goal):
    day += 1
    distance = distance * 1.1

print(f"Ну где-то на {day} день получится")
