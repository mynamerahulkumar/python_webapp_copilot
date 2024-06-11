# single, specfic ,short and surround
#python method using the list and filter the even numbers 
def even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

#python method using lambda function to filter the even numbers
def even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

# pythond method using for loop to filter the even numbers
def even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

#python method using for looop to filter the even numbers and handle the non integer values
def even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if isinstance(number, int) and number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

# assert
assert even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
assert even_numbers([1, 3, 5]) == []
assert even_numbers([2, 4, 6]) == [2, 4, 6]
assert even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]