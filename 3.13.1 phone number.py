phone_number = int(input())

prefix = phone_number // 10000000
mid = (phone_number // 10000) % 1000
last_4 = phone_number % 10000

print(f'({prefix}) {mid}-{last_4}')