# "r" - Read

# "a" - Append

# "w" - Write

# "x" - Create

# "t" - Text

# "b" - Binary

#open & Read File

# f = open('test.txt', 'r') # R - Read

# print(f.name)

# f.close()



with open('test1.txt', 'a') as g:

	g.write('THis is line number 6'+"\n")

	print(g,end='') 