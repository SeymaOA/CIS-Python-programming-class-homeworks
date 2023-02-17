#Calculates the user's age in minutes and seconds.

user_age_years = int(input('Enter your age in years:\n'))
user_age_days = user_age_years * 365
user_age_min = user_age_days * 2460
user_age_sec = user_age_days * 246060
user_heart_beat = user_age_min * 72
user_cal_lifetime = user_age_days * 2470
print(f'You are at least {user_age_days} days old.\nOr \nYou are at least {user_age_min} minutes old')
print(f'Or\nYou are at least {user_age_sec} seconds old.')
print(f'Your heart has beaten totally {user_heart_beat} times.')
print(f'You are gained {user_cal_lifetime} calories in your life time.')