#Задана натуральная степень k. 
#Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random
import math
k=int(input("Введите натуральную степень многочлена"))
a=random.randint(0,100)
b=random.randint(0,100)
c=random.randint(0,100)
x=float
P=a*pow(x,k)+(b*pow(x,k-1))+(c*pow(x,k-2))
data= open('test4.txt','r')
data.writelines(P)
data.close()