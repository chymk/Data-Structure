def spiralOrderMatrix(mat,R,C):
    totalCount = R*C
    RCount,CCount = R,C
    count,r,c = 0,0,0
    while count<totalCount:
        if count ==0:
            print(mat[r][c])
        i = 0
        while i < CCount-1 and count<totalCount:
            c += 1
            print(mat[r][c])
            i += 1
            count+=1
        RCount-=1

        i=0
        while i < RCount and count<totalCount:
            r += 1
            print(mat[r][c])
            i+=1
            count+=1
        CCount-=1

        i = 0
        while i < CCount and count<totalCount:
            c-=1
            print(mat[r][c])
            i+=1
            count += 1
        RCount -= 1

        i = 0
        while i < RCount and count<totalCount:
            r-=1
            print(mat[r][c])
            i+=1
            count += 1


R = 4
C = 4
arr = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
spiralOrderMatrix(arr,R,C)