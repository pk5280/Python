# Write your code here

def vanity(codes, numbers):
    # Check Constraints
    error = 0
    for c in range(len(codes)):
        if codes[c].isupper() is False or codes[c].isalpha() is False or len(codes[c]) > 16:
            print('Code', c + 1, 'must consist of 1 to 15 uppercase letters--', codes[c])
            error += 1
    for n in range(len(numbers)):
        if numbers[n][0] != '+' or len(numbers[n]) >= 17 or numbers[n][1:].isnumeric() is False:
            print('Phone number', n + 1, 'must start with a + followed by no more than 15 numbers to be valid (E.164 format)--', numbers[n])
            error += 1
    if error != 0:
        error_message = ('*** ' + str(error) + ' error(s). Please check HackerRank Debug Output to fix')
        return error_message

    def code2nums(code):  # This part of the code maps our alpha characters to a numeric value
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        transform = '22233344455566677778889999'
        res = ''
        for a in code.lower():  # Here we look at a letter in the code and look at its index in our list alpha
            res += transform[alpha.index(a)]  # We then look at the same index in our transform and add it to our result
        return res

    # dictionary of the values
    def append_value(dict_obj, key, value):
        if key in dict_obj:  # Check that our phone number is already in our dictionary
            if not isinstance(dict_obj[key], list):  # append our new transformed phone number
                dict_obj[key] = [dict_obj[key]]
            dict_obj[key].append(value)
        else:  # If phone number isn't in dictionary add it with our transformed phone number
            dict_obj[key] = value

    answer = {}  # blank list of numbers we plan on returning
    for i in range(len(codes)):  # reference each code
        nums = code2nums(codes[i])  # define our code as numbers
        for j in range(len(numbers)):  # iterate through the possible phone numbers
            if nums in numbers[j]:  # checks that or code is in the phone number
                count = 0
                start = 0
                while start < len(numbers[j]):  # goes through our phone number looking for multiple possibilities of the code
                    pos = numbers[j].find(nums, start)
                    if pos != -1:
                        replacement = numbers[j][:pos] + codes[i] + numbers[j][pos+len(nums):]  # locates code spot in in our phone number and replaces the letters
                        append_value(answer, numbers[j], replacement)  # uses the code to append it to our dictionary
                        start = pos + 1
                        count += 1
                    else:
                        break
    return answer


if __name__ == '__main__':
    # Testing
    x = ['ABCD', 'GGGG']
    y = ['+11a9944441', '+22234444', '+11442223', '+12231133', '+124444411']
    print(vanity(x, y))
