for i in range (1,11):
    print(i)

l1 = []
for i in range (1,21):
    # if i % 2 == 0:
        l1.append(2* i)
        
print(l1)        


list1 = [2*i for i in range (1,1000) if (i%2 == 0)]
print(list1)