# Assigning different different data to different variables
x = 42
y = 3.14
z = 'hello'
# printing the data type of each variable
print(type(x), type(y), type(z))
# output = <class 'int'> <class 'float'> <class 'str'>

# declare string to variable
i = '100'
print(type(i))
# output = <class 'str'>
# converting the variable to integer
converted = int(i)
print(type(converted))
# output = <class 'int'>

# trying to sum int and float
print(x + y)
# output = 45.14

# trying to multiply a string and an int
print(x * z)
# output = the string is repeated 'x' number of times i.e 42

first_num = input('Enter first number: ') # 33
second_num = input('Enter second number: ') # 69
print(type(first_num), type(second_num))
# output = <class 'str'> <class 'str'>

# Convert the result to int
converted_first_num = int(first_num)
converted_second_num = int(second_num)
# print the sum
print(converted_first_num + converted_second_num)
# output = 102
# print the data type
print(type(converted_first_num), type(converted_second_num))
# output = <class 'int'> <class 'int'>


