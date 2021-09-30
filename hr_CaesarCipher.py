
def caesarCipher(s, k):
    # Write your code here
    alpha = "abcdefghijklmnopqrstuvwxyz"
    k = k % len(alpha)
    shifted = alpha[k:] + alpha[:k]
    alpha += alpha.upper()
    shifted += shifted.upper()
    new = ''
    for w in s:
        if alpha.find(w) == -1:
            new += w
        else:
            new += shifted[alpha.index(w)]
    return new


if __name__ == '__main__':
    s = 'middle-Outz'
    k = 2
    print(s, k)
    print(caesarCipher(s, k))
