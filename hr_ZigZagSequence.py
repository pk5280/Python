

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n)/2) #first change to find actual middle - Could aslo do int((n + 1)/2 + 1)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2 #Changed so we don't leave the range
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 #Changed so an actual swap occurs instead of a slide

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7]
    n = 7
    print(a)
    print(findZigZagSequence(a, n))
