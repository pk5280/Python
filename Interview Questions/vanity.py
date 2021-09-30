def vanity(codes, numbers):
    def letters2nums(l):
        if l in 'abc':
            return '2'
        if l in 'def':
            return '3'
        if l in 'ghi':
            return '4'
        if l in 'jkl':
            return '5'
        if l in 'mno':
            return '6'
        if l in 'pqrs':
            return '7'
        if l in 'tuv':
            return '8'
        if l in 'wxyz':
            return '9'

    def code2nums(code):
        lowerCode = code.lower()
        res = ''
        for m in range(len(lowerCode)):
            res = res + str(letters2nums(lowerCode[m]))
        return res

    answer = []
    for i in range(len(codes)):
        nums = code2nums(codes[i])
        for j in range(len(numbers)):
            if nums in numbers[j] and numbers[j] not in answer:
                answer.append(numbers[j])

    return sorted(answer)

if __name__ == '__main__':
    codes = ['ABCD', 'GGGG']
    numbers = ['+12318787', '+19944441', '+11442223', '+12231133', '+12444411']
    print(vanity(codes, numbers))
