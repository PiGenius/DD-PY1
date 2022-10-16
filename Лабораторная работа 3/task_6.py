list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

N = len(list_numbers)

for index, value in enumerate(list_numbers):
    if value == max(list_numbers):
        list_numbers[index], list_numbers[N - 1] = list_numbers[N - 1], list_numbers[index]
        break

print(list_numbers)
