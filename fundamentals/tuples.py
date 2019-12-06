# Python's tuple
# tuples is a sequence of immutable python objects
# just like list but the tuple's object can't be change
# once created, it can never be append or modify

# use parentheses or just comma delimiter only to declare a tuple
vowels = ('a', 'e', 'i', 'o', 'u')
vowels = 'a', 'e', 'i', 'o', 'u'

# iterating to a tuple
# for loop
for vowel in vowels:
    print(vowel)

# concatinating two tuples
alphabets = vowels + ('b', 'c', 'd', 'e', 'f') # .. z

# methods of tuples
# 1. count(param) will return the number of value equal to param
vowels.count('a')

# 2. index(param) will return the index of param
vowels.index('a')

# deleting a tuple
del alphabets

# Python BIT tuple functions
# getting the max value
max(vowels)

# getting the mix value
min(vowels)

# getting the length
len(vowels)
