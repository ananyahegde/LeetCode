"""   Complexity - O(n)

    number = 600851475143
    
    def get_prime_factors (number: int) -> list[int]:
        factor = 2 
        l = []

        while (factor < number):
            if number % factor == 0:
                flag = True
                for i in range (2, factor):
                    if (factor % i == 0): 
                        flag = False 
                        break

                if flag:
                    l.append(factor)
            factor = factor + 1    
        return l

    def get_largest (primes: list[int]) -> int:
        return max(primes) 

    l = get_prime_factors (number)
    print(l)
    lp = get_largest(l)
    print(lp)

Do not think about running this one. It will not run anytime soon. You can see how big that number 'number' is. 
But the solution given is definately correct. You can verify it by giving smaller numbers.
"""

import math
import time 

number = 600851475143

def get_prime_factors (number: int) -> list[int]:
    factor = 2 
    sq = int(math.sqrt(number))
    l = []

    while (factor < sq):
        if number % factor == 0:
            flag = True
            for i in range (2, factor):
                if (factor % i == 0): 
                    flag = False 
                    break

            if flag:
                l.append(factor)
        factor = factor + 1    
    return l

def get_largest (primes: list[int]) -> int:
    return max(primes) 

start = time.perf_counter()
l = get_prime_factors (number)
finish = time.perf_counter()
print(l)
lp = get_largest(l)
print(lp)

print("Finished in ", round((finish-start), 4) ,"Second(s)")

"""
Time complexity: O(_/n)
This is called pollard's rho algorithm. Check out the wiki. 
Also check out Birthday paradox. (Logarithmic?)

"""

"""
We still can optimize it using multiprocessing.

little note: Multi processing is used for CPU bound, i.e., if the CPU is taking time by doing a lot of operations on data.
             Multi threading is used for I/O bound. i.e., reading inputs from the disk, downloading images, etc. They dont use CPU much. 

If you mix em up and use one for another, they may even slow the program because of the overhead. So make sure to use the appropriate one.
"""
