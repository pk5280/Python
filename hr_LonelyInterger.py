#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    res = 0
    for num in a:
        res ^= num
    return res

if __name__ == '__main__':
    arr = [1,1,77,77,2,2,6,99,99,3,3]
    print(arr)
    print(lonelyinteger(arr))