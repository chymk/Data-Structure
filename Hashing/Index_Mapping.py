def search(x):
    if x>=0:
        return has[x][0]
    x= abs(x)
    return has[x][1]
def insert(a,n):
    for i in range(0,n):
        if a[i] >= 0:
            has[a[i]][0] = 1
        else:
            has[abs(a[i])][1]=1

if __name__ == "__main__":

    a = [-1, 9, -5, -8, -5, -2]
    n = len(a)

    MAX = 1000

    # Since array is global, it is
    # initialized as 0.
    has = [[0 for i in range(2)]
           for j in range(MAX + 1)]
    insert(a, n)
    X = -5
    if search(X) == True:
        print("Present")
    else:
        print("Not Present")
