# read the input from console and typecast to string
lineInput = str(input("enter the string"))
# create an empty dictionary
dictionary = {}
# split the words and sort them as well
splitWords = sorted(lineInput.split())
# creating a loop to check for words in split words
for word in splitWords:
    # if word is already present in dictionary then value is incremented by 1 else count will be 1
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

print(dictionary)
