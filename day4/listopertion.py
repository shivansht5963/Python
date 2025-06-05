# append
print("-----------------append------------------")

l1=["mango","banana"]
print("original list:", l1)

l2 =["chiku", "apple"]

l1.append(l2)
print("appended list:", l1)

l1.append("fig")
print("final list:", l1)


# expand
print("-----------------expand------------------")

l1=["mango","banana"]
print("original list:", l1)

l2 =["chiku", "apple"]

l1.extend(l2)
print("extended list:", l1)

l1.extend("BEAR")
print("final list:", l1)

# concatenate
print("-----------------concatenate------------------")
C1 = ["Shivansh"]
C2 = C1 + ["Tiwari"]

print(C2)


# insert and delete

print("-----------------insert and delete------------------")

list1 = ["a","e","i","u"]
list1.insert(3,"o")
print(list1)
list1.remove("a")
print("updated list after removal:", list1)
# list1.remove("z")
print(list1)

#  pop
print("-----------------pop------------------")

list1.pop(3)
print(list1)
list1.pop()
print(list1)


# clear and count
print("-----------------clear and count------------------")

c1 = ["a","b","b","c"]
c1.clear()
print(c1)
c2 = ["a","b","b","c"]

print(c2.count("b"))

# reversing
print("-----------------reversing------------------")

R1= ["Shivansh", "Tiwari"]
R1.reverse()
print(R1)

# index

print("-----------------index------------------")

l1 = ["Fig", "Apple"]
l2 = l1.index("Fig")
print(l2)

# sort

print("-----------------sort------------------")

s1=["a","d","s","p","v"]
s1.sort()
print("assending order:", s1)
s1.sort(reverse=True)
print("Descending order",s1)


print("-----------------sorted------------------")
s2 = sorted(s1)
print("Sorted list :",s2)

print("-----------------Deep copy------------------")

copy1 = ["a","r","c","h","o","q"]
copy2 = copy1
copy2.append("sid")

print("original list: ", copy1)
print("new list: ", copy2)
print(id(copy1))
print(id(copy2))

# print("-----------------Shallow copy------------------")
# 11 ["a","v", "t", "b", "z"] 
# 12 = l1.copy() 
# 12.append("Sid") 
# print("Original List: ",11) 
# print("New List: ",12) 
# print(id(11)) 



