def travel(data,N):
    for r in range(0,N/2):
        for i in range(0,N-1*2*r):
            print( data[r][r] )
