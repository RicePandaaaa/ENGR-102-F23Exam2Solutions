# Assume this is the ordered list
numbers = [1, 2, 4, 5, 6, 7, 8, 10]

# Solution code
def insert_number(number, numbers):
    for i in range(len(numbers)):
        if numbers[i] >= number:
            numbers.insert(i, number)
            return
        
    numbers.append(number)

insert_number(9, numbers)
print(numbers)