#### types ####

# you can get the type of a variable by calling the type() function on it
# we can print that result out by enclosing it in a print statement
# print(type(foo))
# ^this executes from the inside out
# 1. first get the result from type(foo)
# 2. then send that result into the print function
# more about functions in control_flow.py

## SECTION 1: numbers - int, float, complex ##
# int type is just any integer
intExample = -10

# ints will automatically convert to float when you divide
intExample /= 5 # the /= is explained in the operators section
print(type(intExample))
# int literals are exactly what you think they'd be: 0, 15, -26, etc...

# floats are basically decimal numbers
# they can be represented as 0.0, 965.34, -2.0, etc.

# complex numbers have a real and imaginary component
# append j to the end of the imaginary number, and add it to a real number if you wish
complexExample = 10 + 5j
print(complexExample)

i = 1j
print(i * i) # i^2 is -1

## SECTION 2: boolean - the name is based on George Boole, who created an algebraic system for logic ##
# you'll find that a lot of programming is based on this system (also called boolean algebra)
# there are only two boolean literals - True and False
booleanExample = True 
print(booleanExample) # print True
print(not booleanExample) # print False; the expression in the parenthese doesn't change the value of booleanExample, but it does evaluate to False

# booleans are *very* useful in helping you think about larger concepts, like if statements
if booleanExample:
	print('this will execute because booleanExample is True')

## SECTION 3: container types - there are quite a few container types. list, dictionary, string, tuple, set 
# what sets them apart from other types is that they have a variable size, and are composed of a sequence of other types

# lists are an ordered sequence of data
listExample = ['a', 2, 'd'] # you can mix different types in lists

# you can access elements of a list with the brackets operator
# the first element of a list is 0. 
print(listExample[0])
#listExample[3] # be careful when accessing elements of a list. if the element doesn't exist you will get an error

listExample.append(5) # you can append to a list as well.


# dictionaries are a defined by key/value pairs. dictionary literals are defined with curly brackets
# {'key': value}
dictionaryExample = {'HP': 50, 'Attack': 32, 'Defense': 65}

# you can access dictionary elements using keys
dictionaryExample['Defense'] = 1000
print(dictionaryExample['Defense'])

# you can create new elements by assigning a value to an unused key
dictionaryExample['Name'] = 'Lasagna Monster'


# strings are also container types, although they only hold one data type: characters
# string literals are characters enclosed in quotation marks
stringExample = "Kevin's cheet sheet is pretty neat" # single quotes can be used in double quotes without any problem
#wrongString = 'This example string won't work' # the apostrophe in won't gets interpreted as the end of the string

# strings can also be accessed with square brackets
print(stringExample[0])

stringExample = stringExample + ", right?" # you can concatenate strings using the '+' operator
print(stringExample)



