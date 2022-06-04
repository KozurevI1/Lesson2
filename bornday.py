bornyear=input ("Введите год рождения Пушкина А.С.")
if bornyear == "1799":
    print("Верный год")
    date = input("Введите дату рождения:")
    if date == "26,05" or date== "26,5" or date== "05,26" or date =="5,26" or date== "26.5" or date== "05.26" or date =="5.26"or date =="26.5":
        print("Все верно")
    else:
        print("Неверная дата")
else: print ("Неверный год")
