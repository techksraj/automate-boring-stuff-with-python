for i in range(2, 11):
    for num in range(2,i):
        if i%num == 0:
            break
    else:
        print(i)