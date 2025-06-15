"""     This is a program to print first 10 fibonacci terms. 

limit = 4000000
a = 1 
b = 2 
sum = 0 
term = 0

print(a)
print(b)

for i in range(8): 
    term = a + b
    print(term)
    a = b
    b = term 

"""


limit = 4000000
a = 1 
b = 2 
sum = 0 
term = 0

while(term < limit): 
    term = a + b
    if term % 2 == 0:
        sum = sum + term
    a = b
    b = term 

print(sum + 2)