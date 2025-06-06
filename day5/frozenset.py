# creating frozen set
x = frozenset([1,2,3])
y = frozenset([3,4,5])

print("frozen set X :", x)
print("Frox=zen set Y : ", y)

# memebership testing 
print('y' in frozenset ("python"))

# looping througvh frozen set

for ch in frozenset("freeze"):
    print(ch, end= '')
print()

# converstion exxample
my_list = [1,2, 2, 3]

my_set= set (my_list)

my_frozenset = frozenset(my_set)

print("List :", my_list)
print("Set :",my_set)
print("Frozen set : ", my_frozenset)

# Frozenset as dictionary key
f1 = frozenset([1, 2])
f2 = frozenset([2, 3])

frozen_dict = {f1: "first", f2: "second"}
print("Frozen dict:", frozen_dict)
