# take input form the user
password = input("Enter password");

# declare variables
hasNumber = False
hasUpperCase = False
hasLowerCase = False
hasSpecialCharacters = False
hasCorrectLength = True if len(password)> 5 and len(password)< 17 \
    else False
# loop to set all variables according to condition
if hasCorrectLength:
    for temp in password:
        if temp.isupper():
            hasUpperCase = True
        if temp.islower():
            hasLowerCase = True
        if temp.isnumeric():
            hasNumber = True
        if temp in "[$@!*]":
            hasSpecialCharacters = True
else:
    print("Password must have a minimum length of 6 and maximum length of 16")

# validation with the predefined conditions for validating password
if hasSpecialCharacters and hasNumber and hasUpperCase and hasLowerCase:
    print("Password created successfully")
else:
    print("Please check the rules for password criteria")

