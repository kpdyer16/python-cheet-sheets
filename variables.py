#### variables ####

# create newVar and assign 20 to it (int)
newVar = 20

# create guide and assign "cheat sheet" to it (string)
guide = 'cheat sheet'

# create lis and assign ['a','b','c','d'] to it (list)
# notice the elements of the list are strings
lis = ['a', 'b', 'c', 'd'] 

guide = lis # guide now holds the same object as list
print('print guide:')
print(guide)

# access list elements with square brackets []
guide[2] = 'z' # first element is always 0. so guide[2] will access the third element ('c')
print('guide[2] = z:') # print guide
print(guide)

# what do you think print(lis) will print out?
#print(lis) # uncomment this print statement to find out
			# why do you think this happens?
