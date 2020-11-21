print("Все теперь играем в бизенес :)")
print("Давай типа я Главбух на аутсорсе. Поехали")
debit = int(input("Че по доходам у нас? >>>"))
credit = int(input("А тратим сколько? >>>"))
profit = debit - credit
if debit > credit:
    print(f"Кароч все путем. Наша прибыль {profit}")
    print(f"Рентабильность при этом {(profit / debit)*100}%")
    humans = int(input("Так, а человеков у нас сколько? >>>"))
    print(f"Это выходит примерно по {profit // humans} на человечка. Не кисло")
elif credit > debit:
    print(f"Ничего не перепутал? у нас убыток {profit}. Попробуй еще раз")
