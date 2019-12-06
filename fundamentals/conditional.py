# python's conditional expression

x = 1
y = 0
# if-else
if x > y:
    print("x is greater than y")
elif x < y:
    print("y is greater than x")
else:
    print("y and x are equal of value")


# ternary if in python can be used on another expression
greaterValue = (x if(x > y) else y) + 2
# this can be read as "the greaterValue is x if it's greater than y else y, then add 2"
print(greaterValue)


# no switch expression in python :) but its posible to implement
# a function that behave the same as switch expression

