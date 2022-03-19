from ast import Num


listOfNumber = []
while(1):
    num = int(input('Enter your no. : '))
    if(num == -1):
        break
    listOfNumber.append(num)
max = 0
min = 0
for i in range(0, len(listOfNumber)-1):
    print(listOfNumber[i])
    if listOfNumber[i] < listOfNumber[i+1]:
        if(min < listOfNumber[i]):
            min = listOfNumber[i]
            max = listOfNumber[i+1]
    else:
        max = listOfNumber[i]
        min = listOfNumber[i+1]

print('Max = ' + str(max))
print('Min = ' + str(min))
