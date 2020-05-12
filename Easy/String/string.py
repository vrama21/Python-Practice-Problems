# Functions corresponding to string manipulation

# Convert the string to an integer
def convertToInt(string):
    return int(string)

# Return true if a string is empty, else return false
def isStringEmpty(string):
    if string == "":
        return True
    else: 
        return False

# Concatenate two strings
def concatenate(string1, string2):
    return string1 + string2

# Return the length of a string
def strLength(string):
    return len(string)

# Separate a string by whitespaces into an array
def separateString(string):
    return string.split()

# Join a list of strings into a single string by white spaces
def joinString(listOfStrings):
    return " ".join(listOfStrings)

    