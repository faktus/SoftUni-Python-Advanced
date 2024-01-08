numbers = input().split()

reversed_numbers = [numbers[number] for number in range(len(numbers) - 1, -1, -1)]
print(' '.join(reversed_numbers))