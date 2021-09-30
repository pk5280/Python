
def caesarCipher(s):
    # Write your code here
    alpha = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    shifted = '2222223333334444445555556666667777777788888899999999'
    new = ''
    for w in s:
        new += shifted[alpha.index(w)]
    return new


if __name__ == '__main__':
    s = 'ABCD'
    print(s)
    print(caesarCipher(s))
