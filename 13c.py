num = 7
for i in range(1, num+1):
    for j in range(1, num):
        if j < num and j >= num+1-i:
            print(num-j, end=' ')
        elif j == num:
            print(1, end=' ')
        else:
            print(" ", end=' ')
    print()
