for j in range(1,10):
    for i in range(1,j+1):
        if i==j:
            print(j*i,end='')
        else:
            print(j*i,end=',')
    print('')