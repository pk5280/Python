def miniMaxSum(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]

    maxNum = sum - min(arr)
    minNum = sum - max(arr)

    print(minNum, maxNum)
    # Write your code here

if __name__ == '__main__':
    arr = [1,1,0,1,2,5,6]
    print(arr)
    print(miniMaxSum(arr))