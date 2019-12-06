# Python's Loops

# while loop
# while loop execute a set of commands as long as the condition is true
number = 1
while number <= 10:
    if((number%2) == 0):
        print(number)
    number += 1


# for loop
# for loop is used to iterate mostly on list, string, truples, set, and dictionary
movies = ["Titanic", "Attack on titan live action", "Lion King"]
for movie in movies:
    print(movie)