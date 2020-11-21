userSec = int(input("Пс-с, да ты. Смотри магию покажу. Введи любое количество секунд >>>"))
hours = userSec // 3600
minuts = (userSec % 3600) // 60
seconds = (userSec % 3600) % 60

print(f"Зацени! это получается {hours}:{minuts}:{seconds}")