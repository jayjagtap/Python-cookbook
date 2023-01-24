"""
yield behaves like a return statement with a slight difference. 
yield returns a generator object to the function which calls it (generator function)

yield functions returns one value, waits, saves the local state and resumes again
You can iterate over a generator object or convert it into list

yield saves the memory as opposed to storing everything in a list and retutning with a return statement

Generators follow lazy intialization, which means it loads an object only when it is needed.
This orevents unnecessary memory usage and improves performance.

"""

# Example 1
#Fibonacci series using a generator object

def fibonacci_generator(nth):
    prev, curr = 0, 1
    counter = 0

    while counter < nth:
        if curr%2 != 0:
            yield curr
        temp = curr
        curr = curr + prev
        prev = temp

        counter+=1

# Print the list using the generator function with a condition of printing only odd numbers

def print_fibo_odd(n):
    # Lazy evaulation
    my_gen = fibonacci_generator(n)

    for i in my_gen:
        print(i)

print_fibo_odd(15)

# Example 2
# Returning a range of floating point numbers

def range_generator(start, end, step):
    curr = start
    while curr <= end:
        yield curr
        curr = curr + step

# Returning as a list robs it off the memory advantage it gives, so this is not a suitable example to be using yield
print("Range Generator: ", list(range_generator(2, 22, 3.5)))

# Example 3
# Return a list of cubes given start and end numbers

def cubes_generator(start, end):
    for i in range(start, end+1):
        yield i*i*i

print("Cubes bw 5 and 13 are: ", list(cubes_generator(5, 13)))


# Program Output
# jayjagtap@ip-10-0-0-175 ~ % /usr/local/bin/python3 /Users/jayjagtap/Desktop/MyBooks/Python-cookbook/Chapter1/yield_exploration/yield_examples.py
# 1
# 1
# 3
# 5
# 13
# 21
# 55
# 89
# 233
# 377
# Range Generator:  [2, 5.5, 9.0, 12.5, 16.0, 19.5]
# Cubes bw 5 and 13 are:  [125, 216, 343, 512, 729, 1000, 1331, 1728, 2197]




