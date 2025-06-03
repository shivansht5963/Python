# implicit typecasting
num_int = 2
num_float = 67.56789
sum=num_int+num_float
print(sum)
print("num 1 = ", num_int, "and its type is :",type(num_int) )
print("num 2 = ", num_float, "and its type is :",type(num_float) )
print("sum is  = ", sum, "and its type is :",type(sum) )

#explicit type casting 


int1 = 20
str = "67"
print("num 1 = ",int1, "and its type is :",type(int1) )
print("num 2 = ", str, "and its type is :",type(str) )
print("sum of two differnt data type is", int1 + int (str) )