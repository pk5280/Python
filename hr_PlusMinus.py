#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else:
            zero += 1

    print('%f' % (pos / len(arr)))
    print('%f' % (neg / len(arr)))
    print('%f' % (zero / len(arr)))

if __name__ == '__main__':
    arr = [1,1,0,-1,-1]
    print(arr)
    print(plusMinus(arr))
