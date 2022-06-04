flag=True
while True:
        
    if flag:
        
        bornyear=input ("Введите год рождения Пушкина А.С.")
        
        if bornyear == "1799":
            print("Верный год", end="\n\n")
            flag=False

        else:    
            print ("Неверно", end="\n\n")

    else:

        date = input("Введите дату рождения:")

        if date == "26,05" or date== "26,5" or date== "05,26" or date =="5,26" or date== "26.5" or date== "05.26" or date =="5.26"or date =="26.5":
            print("Все верно", end="\n\n")
            break
        
        else:
            print("Неверная дата", end="\n\n")
