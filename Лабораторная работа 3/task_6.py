list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

i = 0
while list_numbers[i] != max(list_numbers):
    i += 1
list_numbers[i], list_numbers[-1] = list_numbers[-1], list_numbers[i]

print(list_numbers)
