#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    n = len(matrix)
    n_sub = int(n / 2)
    m = [0] * (n_sub * n_sub)
    cnt = -1
    for i in range(n_sub):
        for j in range(n_sub):

            cnt = cnt + 1
            tmp = [matrix[n - (i + 1)][j], matrix[i][n - (j + 1)], matrix[n - (i + 1)][n - (j + 1)]]

            if matrix[i][j] > max(tmp):
                m[cnt] = matrix[i][j]
            else:
                m[cnt] = max(tmp)
    return sum(m)

if __name__ == '__main__':
    matrix = ([1,2], [3,4])
    print(matrix)
    print(flippingMatrix(matrix))