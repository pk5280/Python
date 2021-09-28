#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    newarr = sorted(arr)
    print(newarr)
    middle = len(arr)//2
    print(middle)
    return newarr[middle]
    # Write your code here


if __name__ == '__main__':
    arr = [1,1,0,1,2,5,6]
    print(arr)
    print(findMedian(arr))
