# dic={"A":1,"B":2}
# print(dic.get("A"))
# print(dic.get("C"))
# print(dic.get("C", "not found!"))

# # pop
# d1={1:"a",2:"b",3:"c",4:"d"}
# d1.pop(4)
# print(d1)

# # del\\

# d1={}
# del d1
# # print(d1)

# d1={1:"a",2:"b",3:"c",4:"d"}
# del d1[4]
# print(d1)

# d1={1:"a",2:"b",3:"c",4:"d"}
# d1.clear()
# print(d1)

# # update it can also work as python

# lang1 = {1:"c",2:'C++',3:'java',4:'python'}

# lang2={5:'VB',6:'FORTRAN'}

# lang1.update(lang2)
# print(lang1)

# lang3 = {1:'PHP',7:'perl'}

# lang1.update(lang3)
# print(lang1)



# len() keys(_) value() item()

lang={1:'c',2:'C++',3:"java",4:'python'}

print(len(lang))
print(lang.keys())
print(lang.values())
print(lang.items())



# key as value and value as key 
b_dict={}
a_dict={'one':1,'two':2,'three':3,'four':4}
for key,value in a_dict.items():
    b_dict[value]=key
print(b_dict)