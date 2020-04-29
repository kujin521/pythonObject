for j in range(2,10):
    m=0
    for i in range(2,j):
        m=i
        if j%i==0:
            break
    if m==j-1:
        print(j)