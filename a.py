import random

bot_number = random.randint(1, 3)
user_number = int(input("Введите число от 1 до 10: "))
if user_number == bot_number:
    print("Вы угадали!")
else:
    print("Вы не угадали. Попробуйте еще раз.")
