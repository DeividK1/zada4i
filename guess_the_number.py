import random

def guess_the_number():
    # Генериране на случайно число между 1 и 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Познай числото, което съм избрал (между 1 и 100)!")

    while True:
        # Въвеждане на предположение от потребителя
        guess = int(input("Въведи твоето предположение: "))
        attempts += 1
        
        # Проверка на предположението
        if guess < secret_number:
            print("Твоето число е по-малко. Опитай пак.")
        elif guess > secret_number:
            print("Твоето число е по-голямо. Опитай пак.")
        else:
            print(f"Поздравления! Позна числото {secret_number} за {attempts} опита.")
            break

# Стартиране на играта
guess_the_number()
