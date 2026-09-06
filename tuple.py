# create a tuple with different data types
tuplex=("tuple",False,3.2,1)
print(tuplex)

#create a tuple
tuplex=(4,6,2,8,3,1)
print(tuplex)

# tuple is immutable, so we can not add new elements
tuplex = tuplex + (9,)
print(tuplex)

# count the number of occurrences of item 50 from a tuple
tuple1=(50,10,60,70,50)
print(tuple1.count(50))

# create a tuple 
tuplex=(2,4,3,5,4,6,7,8,6,1)
# use tuple[start:stop] the start index is inclusive and the stop index 
_slice= tuplex[3:5]
#is exclusive
print(_slice)
#if the start index is not defind, is taken from beg inning of the tuple
_slice= tuplex[:6]
print(_slice)

