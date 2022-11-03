from random import shuffle

def get_unique_list_numbers() -> list[int]:
    available_range = [n for n in range(-10, 11)]
    shuffle(available_range)
    return available_range[:15]


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
