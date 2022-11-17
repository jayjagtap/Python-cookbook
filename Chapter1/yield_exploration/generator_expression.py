"""
Generators fascinated me, so here I am learning more about them

Generators can be used in place of arrays to save memory. 
This is because generators do not store the values, but rather the computation logic 
with the state of the function, similar to an unevaluated function instance ready to be fired.

i.e Initialization of an object would be done only when it is needed not before 

Use Cases:
1. We work with huge amount of data and do not need to load all of it in memory at once.
2. The cost of object creation and storage is very high and the utilisation of the same object is rare.

Reference Article: https://medium.com/swlh/writing-memory-efficient-programs-using-generators-in-python-49854bb57da6
"""

from sys import getsizeof
import time
# List comprehension vs Generator comprehension
num_list  = [num*num for num in range(1000000)]
generator_num = (num*num for num in range(1000000))

print(f"Memory of the list for 1 million numbers: {getsizeof(num_list)} bytes")
print(f"Memory of the Generator of 1 million numbers:  {getsizeof(generator_num)} bytes")
print(f"Convert the generator to list now: {getsizeof(list(generator_num))} bytes")

# Output
# Memory of the list for 1 million numbers: 8448728 bytes
# Memory of the Generator of 1 million numbers:  112 bytes
# Convert the generator to list now: 8448728 bytes

"""
From the above example, the generator does the following:
1. Does not block memory until needed, you can convert it to a list when actually needed.
2. More efficient than converting the generator object to list would be to have a use case where the generator 
could be iterated
"""

generator_num = (num*num for num in range(1000000))
for i in range(10):
    print(next(generator_num))

