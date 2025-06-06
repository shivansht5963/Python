# set operations

# creating set 

a = {1,2,3,4}
b = set([3,4,5,6])
c= set({1:"sid"})

print("Set A:", a)
print("Set B:", b)
print("Set C:", c)

# adding elements
a.add(10)
print("After adding 10 to A:", a)

# upodating multiple elemnets
a.update([11,12])
print("After Updating A with [11, 12]:", a)

# removinbg elements

a.remove(10)
a.discard(100)
print("after removing 10 and discarding 100: ", a)

print("A: ",a)
print("B: ", b)

# set uninon

print("Union: ", a|b) #or a.union(b)

# set intersection

print("Intersection: ", a & b ) #or a.intersection(b)

#  set differnce 
print("Differnce A- B: ", a-b  )

# Set symmetric differc=nce 
print("Symmetric Differnce :", a^b)

# subset and super set 
print("A is subset of  b :", a.issubset(b))
print("A is super set of B :", a.issuperset(b))

# coping and clearing 
c = a.copy()
print("Copy of A : " , c)

c.clear()
print("cleared set :", c)
