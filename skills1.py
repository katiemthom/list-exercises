# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    odds = []
    for value in some_list: 
        if value % 2 == 0: 
            pass
        else:
            odds.append(value) 
    return odds

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    evens = []
    for value in some_list: 
        if value % 2 == 0: 
            evens.append(value)
    return evens

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    long_words = []
    for word in word_list: 
        if len(word) > 4: 
            long_words.append(word)
    return long_words

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    smallest = some_list[0]
    for value in some_list: 
        if value < smallest: 
            smallest = value
    return smallest

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    largest = some_list[0]
    for value in some_list: 
        if value > largest: 
            largest = value
    return largest

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    halvesies = []
    for value in some_list: 
        halvesies.append(value/2)
    return halvesies

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lenths(word_list):
    lengths = []
    for word in word_list: 
        lengths.append(len(word))
    return lengths

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    sum_vals = 0
    for value in numbers: 
        sum_vals += value
    return sum_vals

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    product = 1
    for value in numbers: 
        product *= value
    return product

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    joined = ""
    for string in string_list: 
        joined += string
    return joined 

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    total = 0
    for value in numbers: 
        toal += value
    avg = total/len(numbers)
    return avg
