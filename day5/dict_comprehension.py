# dic1 = {"a":1,"b":2,"c":3}
# d1={k:v for (k,v) in dic1.items() }
# print(d1)

dic1 = {"a":1,"b":2,"c":3,"d":4,"e":5}
d2 = {k:v for(k,v) in dic1.items() if v%1==0}
print(d2)

dic1 = {"a":1,"b":2,"c":3,"d":4,"e":5}
d2 = {k:("even" if v%2==0 else "odd") for k, v in dic1.items()}

print(d2)