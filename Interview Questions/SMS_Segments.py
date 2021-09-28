def segments(message):
    answer = []
    wordBreak = 0 # Finding the Spaces
    wordStart = 0 # Finding the start of word
    totalMessages = 0 # Total number of messages that will be sent
    character = 0 # The Character in the messasge we are on
    i = 0
    while i < len(message): # Set a range of i that is less than the length of the message so we don't go out of range
        character += 1
        if message[i] == ' ': # The code that identifies where a word break exists by looking for the last space
            wordBreak = i
        if character == 155: # we look up until the 155th character because the max appendage we have is (9/9) and that is 5 additional characters so we have to remove 5 from 160
            if message[i] != ' ': # here we itterate backward through the characters until we find the last wordBreak thne we mark the wordBreak at that point
                if (i < len(message) - 1 and message[i + 1] == ' ') or i == len(message) - 1:
                    wordBreak = i
            totalMessages += 1 # Here we add that there will be an additional message
            character = 0
            answer.append(message[wordStart:wordBreak + 1]) #Here we append the first message to our list answer
            if i > wordBreak:
                i = wordBreak
            wordStart = i + 1
        i += 1
    if wordStart < len(message): #here is where we finish the last message if the characters are less than 155
        if totalMessages == 0:
            return [message]
        answer.append(message[wordStart:])
        totalMessages += 1
    for i, s in enumerate(answer):
        if totalMessage == 1: #we do not send any special suffix if the message is not beyond 1 segment
            answer[i] = message
        else:
            answer[i] = s + '(' + str(i + 1) + '/' + str(totalMessages) + ')' #Here is where we add our (x/y) part of the message after each segment
    return answer


if __name__ == '__main__':
    first = 'Python is an easy to learn powerful programming language It has efficient high-level data structures and a simple but effective approach to objectoriented programming Python elegant syntax and dynamic typing'
    print(solution(first))
