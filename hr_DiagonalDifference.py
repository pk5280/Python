#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    d1 = 0
    d2 = 0
    for i in range(len(arr)):
        d1 = d1 + arr[i][i]
    for j in range(len(arr)):
        d2 = d2 + arr[j][len(arr) - 1 - j]
    dif = abs(d1 - d2)

    return dif

if __name__ == '__main__':
    arr = ( [11,2,4],[5,5,6],[10,8,-12])
    print(arr)
    print(diagonalDifference(arr))