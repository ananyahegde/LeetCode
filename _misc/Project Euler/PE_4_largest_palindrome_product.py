'''import  itertools
import time 

palindrome_list = []
start = time.perf_counter()

def get_lists(number: int) -> tuple[list[int], list[int]]:
    rev_digits = []

    while (True): 
        rem = number % 10
        rev_digits.append(rem)

        if number//10 == 0: 
            break
        quo = number // 10 
        number = quo  

    n = len(rev_digits)
    digits = [0] * len(rev_digits)

    for i in range(n): 
        digits[n-i-1] = rev_digits[i] 

    return digits, rev_digits

pairs = itertools.product(range(100, 1000), repeat=2)
products = [a * b for a, b in pairs]

for i in range(len(products)):

    product = products[i]
    li, rev_li = get_lists(product)
    
    if li == rev_li and li!= [] and rev_li!= []: 
        palindrome_list.append(product)
    
print(max(palindrome_list))
end = time.perf_counter()
print("Total time: ", end - start)
'''

# The code works, but no good at all. It doesn't have a proper structure and not readable. Cannot decrease the time complexity ig, but can use multiprocessing? 
# I'll come back later.

import time 

def get_lists(number: int) -> tuple[list[int], list[int]]:
    rev_digits = []

    while (True): 
        rem = number % 10
        rev_digits.append(rem)

        if number//10 == 0: 
            break

        quo = number // 10 
        number = quo  

    n = len(rev_digits)
    digits = [0] * len(rev_digits)

    for i in range(n): 
        digits[n-i-1] = rev_digits[i] 

    return digits, rev_digits

if __name__ == '__main__':

    palindromes = []
    start = time.perf_counter()
    a = 999
    largest_palindrome_product = 0

    while (a > 99): 
        b = 999
        while (b > 99):

            product = a * b
            digits, rev_digits = get_lists(product)
            
            if digits == rev_digits and digits!= [] and rev_digits!= []: 
                if product > largest_palindrome_product: 
                    largest_palindrome_product = product            
            b = b - 1
        a = a - 1
        
    print(largest_palindrome_product)
    end = time.perf_counter()
    print("Total time: ", end - start)


### But this can be improved even further
'''
"All palindromes with an even number of digits are divisible by 11." 

Our scope is only 6 digit number, let's prove only that one. 

let n be of the form ABCCBA (A palindrome) where A, B, and C are (not necessarily distinct) integers such that, 
    1 ≤ A ≤ 9, 0 ≤ B ≤ 9 and 0 ≤ C ≤ 9.

n can be written as: 
    n = 100000A + 10000B + 1000C + 100C + 10B + A
    n = 100001A + 10010B + 1100C 
    n = 11 (9091A + 910B + 100C)

So the 6 digit palindrome we are looking for is divisible by 11. 
Hence, either a or b is divisible by 11. 
'''


import time 

def get_lists(number: int) -> tuple[list[int], list[int]]:
    rev_digits = []

    while (True): 
        rem = number % 10
        rev_digits.append(rem)

        if number//10 == 0: 
            break

        quo = number // 10 
        number = quo  

    n = len(rev_digits)
    digits = [0] * len(rev_digits)

    for i in range(n): 
        digits[n-i-1] = rev_digits[i] 

    return digits, rev_digits

if __name__ == '__main__':

    palindromes = []
    start = time.perf_counter()
    a = 999
    largest_palindrome_product = 0

    while (a > 99): 
        b = 999
        while (b > 99):
            if (a % 11 == 0 or b % 11 == 0):
                product = a * b
                digits, rev_digits = get_lists(product)
                
                if digits == rev_digits and digits!= [] and rev_digits!= []: 
                    if product > largest_palindrome_product: 
                        largest_palindrome_product = product            
            b = b - 1
        a = a - 1
        
    print(largest_palindrome_product)
    end = time.perf_counter()
    print("Total time: ", end - start)
