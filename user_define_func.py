# Adding loops and branches to the function
size = 5
def get_numbers(num):
    numbers = []
    user_input = input(f'Enter {num} integers:\n')

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    print('Numbers:', end=" ")
    for k in numbers:
        print(f'{k}', end=" ")
    print()

def print_odd_numbers(numbers):
    print('Odd numbers:', end=" ")
    for l in numbers:
        if l % 2 != 0:
            print(f'{l}', end=" ")
    print()

def print_negative_numbers(numbers):
    # Print all negative numbers
    print('Negative numbers:', end=" ")
    for m in numbers:
        if m < 0:
            print(f'{m}', end=" ")
    print()
nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)
