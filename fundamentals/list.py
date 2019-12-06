# python list
# a list is a dynamic data holder
# list is like array

# use brackets to declare a list
movies = ["Titanic", "Monster University", "The Lonewolf", "Despicable Me"]

# iterating to a list
# for loop
for movie in movies:
    print(movie)

# BIT of python list
# 1. append(value)
# append() BIT will append a value to the last
# position of the list
movies.append("Mowgli")

# 2. remove(value)
# remove() will remove an item on a list matching
# a given value
movies.remove("Titanic")

# 3. pop()
# pop() will remove the last item on a list
movies.pop()

# 4. insert(position, value)
# insert() will insert a value in a specific position.
# note: just like array, python's list also starts at 0.
movies.insert(0, "Hercules")

# 5. extend(list)
# exted() BIT will merge the existing list with the given
# list value.
movies.extend(["I'am Frankenstein", "The Lord of the Rings: Fellowship of The Ring"])

# 6. clear()
# clear() removes all the data in the list
movies.clear()

# 7. reverse()
# reverse() will reverse the index from last to first
movies.reverse()

# 8. sort()
# sort() will arrange the value of the list in place
movies.sort()

