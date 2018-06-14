# input from user
sentence = input("Enter input sentence:")

# list of all words split by a space delimiter
words = sentence.split(" ")

# initialising variables
maxLength = 0
longestWord = ""
wordsLen = len(words)  # length function 6
# print(wordsLen)
index = 0
middleLengthIndex = 0
reverseSentence = list()
middleWords = []

# To get middle indexes of middle words
if wordsLen % 2 == 0:
    middleLengths = [wordsLen // 2 - 1, wordsLen // 2]
else:
    middleLengths = [wordsLen // 2]

# print(middleLengths) [2, 3]

#  iterate the words
for word in words:
    wordLen = len(word)

    #get max length word
    if wordLen > maxLength:
        maxLength, longestWord = wordLen, word

    # get middle words
    if len(middleLengths) > middleLengthIndex and index == middleLengths[middleLengthIndex]:
        middleWords.append(word)
      # print(middleWords)
        middleLengthIndex += 1
   # print(middleLengthIndex)
    word = word[::-1]
    reverseSentence.append(word)
    index += 1

# joining words
reverseSentence = ' '.join(reverseSentence)
middleWords = ' '.join(middleWords)

# print the required output
print("Middle words:", middleWords)
print("Longest word:", longestWord)
print("Sentence with reverse words:", reverseSentence)
