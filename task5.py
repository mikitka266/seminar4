#В первой строке находятся целые числа M и N (1  ≤ M ≤ N ≤ 1 000 000).
M=int(input("Введите первое целое число "))
N=int(input("Введите второе целое число "))
sumN=0
sumM=0
for i in range(1,M):
    if M%i==0:
        sumM+=i
for j in range(1,N):
    if N%i==0:
        sumN+=j
if(sumM==N and sumN==M):
    print("Числа Дружественны")
else: 
    print({sumN})