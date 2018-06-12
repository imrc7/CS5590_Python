#method1 using set

# take input form user
string=input("Enter string:")
# declare a set with vowels
vowels=set("aeiouAEIOU")
# initialise a counter with value 0
count=0

# iterating the input and comparing with the set of vowels
for i in string:
    if i in vowels:
            count=count+1
print("Number of vowels are:")

# print the output
print(count)



##method 2 without using set

# string=input("Enter string:")
# count=0
# for i in string:
#     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#
#             count=count+1
# print("Number of vowels are:")
# print(count)