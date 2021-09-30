import re

# Write your code here

def vanity(codes, numbers):
    # Check Constraints
    error = 0
    for c in range(len(codes)):
        if codes[c].isupper() == False or codes[c].isalpha() == False or len(codes[c]) > 16:
            print('Code', c + 1, 'must consist of 1 to 15 uppercase letters--', codes[c])
            error += 1
    for n in range(len(numbers)):
        if numbers[n][0] != '+' or len(numbers[n]) >= 17:
            print('Phone number', n + 1, 'must start with a + followed by no more than 15 numbers to be valid (E.164 format)--', numbers[n])
            error += 1
    if error != 0:
        errorMessage = ('*** ' + str(error) + ' error(s). Please check HackerRank Debug Output to fix')
        return errorMessage


    def code2nums(code):  # This part of the code maps our alpha characters to a numeric value
        # alpha = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
        # transform = '2222223333334444445555556666667777777788888899999999'
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        transform = '22233344455566677778889999'
        res = ''
        for a in code.lower():  # Here we look at a letter in the code and look at its index in our list alpha
            res += transform[alpha.index(a)]  # We then look at the same index in our transform and add it to our result
        return res

    answer = []  # blank list of numbers we plan on returning
    for i in range(len(codes)):  # reference each code
        nums = code2nums(codes[i])  # define our code as numbers
        for j in range(len(numbers)):  # iterate through the possible phone numbers
            if nums in numbers[j] and numbers[j] not in answer:  # check that phone number contains code numbers & doesn't exist in list already
                answer.append(numbers[j])  # add the phone number to our answer list
            if nums in numbers[j]:
                count = 0
                start = 0
                while start < len(numbers[j]):
                    pos = numbers[j].find(nums, start)
                    if pos != -1:
                        replacement = numbers[j][:pos] + codes[i] + numbers[j][pos+len(nums):]
                        answer.append(replacement)
                        start = pos +1
                        count += 1
                    else:
                        break

    return sorted(answer)  # sorted answers


if __name__ == '__main__':
    codes = ['ABCD', 'GGGG']
    #numbers = ['+124444411']
    numbers = ['+119944441', '+22234444', '+11442223', '+12231133', '+124444411']
    print(vanity(codes, numbers))
