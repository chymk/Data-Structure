def spiralOrderMatrix(mat,R,C):
    top,down,left,right,dir = 0,R-1,0,C-1,0
    while top <= down and left <= right:
        if dir == 0:
            for i in range(left,right+1):
                print(mat[top][i])
            top+=1
        elif dir == 1:
            for i in range(top,down+1):
                print(mat[i][right])
            right-=1
        elif dir == 2:
            for i in range(right,left+1,-1):
                print(mat[down][i])
            down-=1
        elif dir==3:
            for i in range(down,top+1,-1):
                print(mat[i][left])
            left+=1
        dir = (dir+1)//4


R = 4
C = 4
arr = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
spiralOrderMatrix(arr,R,C)