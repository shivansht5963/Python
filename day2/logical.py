x=5
y=6
z=1

print("x>y and y>z = ",x>y and y>z)
print("x>y or y>z = ",x>y or y>z)


print("x<y and y<z = ",x<y and y<z)
print("x<y or y>z = ",x<y or y>z)


a = True
print(not a)


b1= True
b2= False

print("b1 and b2 is", b1 and b2)
print("b1 or b2 is ", b1 or b2)
print("b1 is not ", not b1)

'''
notes----------------

AND T T = T
OR  T T = T
    T F = T
    
NOT T/F = T/F
XOR T T = F
    T F = T
    
    
    
    
A B | A OR B | A XOR B
------------------------
0 0 |   0    |    0
0 1 |   1    |    1
1 0 |   1    |    1
1 1 |   1    |    0



'''