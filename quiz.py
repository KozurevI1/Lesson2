print("Давайте ответим на несколько вопросов")

while True:
    right_ansver=0
    year1=input("Введите год рождения Пушкина А.С. ") #1799
    if year1=="1799":
        right_ansver+=1

    year1=input("Введите год рождения Моцарта В.А. ") #1756
    if year1=="1756":
        right_ansver+=1

    year1=input("Введите год рождения Ленина В.И ") #1870
    if year1=="1870":
        right_ansver+=1

    year1=input("Введите год рождения Цоя В.Р. ") #1962
    if year1=="1962":
        right_ansver+=1
    
        print("")
    print("Количество правильных ответов = ", right_ansver)
    print("Количество ошибок = ", 4-right_ansver)
    print("Процент правильных ответов = ", right_ansver*100/4,"%")
    print("Процент неправильных ответов = ", (4-right_ansver)*100/4,"%",end="\n\n")

    if input("Хотите пройти квиз снова? y/n ") == "n":
        break
    else:
        print("")
    







