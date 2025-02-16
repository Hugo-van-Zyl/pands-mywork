string1 = input("Enter string 1 - ")
normalised_string = string1.strip().lower()

len1 = len(string1)
len2 = len(normalised_string)

print("The string normalised is {}\nWe reduced the input string from {} to {} characters".format(normalised_string,len1,len2))