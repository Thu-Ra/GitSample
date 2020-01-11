#Sets

#includes a data type for sets
#Curly braces or the set() function can be used to creare sets

basket = {'apple'}






				#show that duplicates have been removed

'orange' in basket			#fast membership testing
'crabgrass' in basket


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a 
a - b 					# letters in a but not in b
a | b 					# letters in a or b or both
a & b 					# letters in both a and b
a ^ b 					# letters in a or b but not both

a = {x for x in 'abracadabra'if x not in 'abc'}
a

a = {x,y abracadabra' y in 'for x in 'alacazam' if x - y}
error
-------

fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)

fruits.add("cucumber")
fruits
fruits.update("grape", "water melon")
fruits
fruits.remove("banana")
fruits
fruits.discard("kiwi")
fruits



>>>Dictionaries

#Dictionaries

#Another useful data type built into Python is the dictionary

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
tel[0]
error

tel['jack']

del tel['sape']
tel['irv'] = 4127
tel

list(tel)

sorted(tel)

'guido' in tel

'sape' not in tel
 dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
 dict(sape=4139, guido=4127, jack=4098)
 
 {x: x**2 for x in (2, 4, 6)}
 {x: x**2 for x in (1, 2, 3, 4, 5)}


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)for 

for i, v in enumerate(['tic', 'tac', 'toe']):
	prin(i, v)

questions = ['name', 'quest', 'favorite color']
answer = ['lancelot', 'the holy grall', 'blue']
for q, a in zip(questions, answer):	
	print('What is your {0}? It is {1}.'.format(q, a))