#Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой,
#  сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)
n=int(input("Введите количество знаков после запятой "))
p="3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337"
for i in range(2,len(p)):
    if n==i:
        print(p[:n+2])
