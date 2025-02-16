'''
6. Question
message = 'I have eaten ' + 99 + ' burritos.'
print (message)
'''
#The above code gives an error because python can only combine like for like. Therefore, changing 99 to a string instead of a value should solve this. 
# 6. Solution Code
message = 'I have eaten ' + '99' + ' burritos.' #or alternatively can use str(99) function
print (message)

# 7. Question - Why is eggs a valid variable name while 100 is invalid? 
# 7. Solution - eggs is a name assigned in the memory to store the value of 100. 100 would not be a very descriptive variable name as this would be the value answer

# 8. Question -What three functions can be used to get the integer, floating-point number, or string version of a value?
# 8. for integer use int() function, for float use float() function, for string use str() function

