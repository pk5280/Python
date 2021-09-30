def towerBreakers(n, m):
    if m==1:
        return 2
    else:
        return 2 if n%2==0 else 1

if __name__ == '__main__':
    n = 3
    m = 2
    print(n,m)
    print(towerBreakers(n, m))

    n = 4
    m = 5
    print(n,m)
    print(towerBreakers(n, m))