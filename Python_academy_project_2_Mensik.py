import random


def main():
    greeting()
    secret_num = secret_number()
    print(secret_num)
    attempt = 0

    while secret_num:
        attempt += 1
        user_num = guess(secret_num)
        bulls, cows = counting(user_num, secret_num)
        finish(bulls, cows, secret_num, attempt)


def greeting():
    print("""
Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
""")


def secret_number():
    secret_num = "".join(random.sample("0123456789", 4))
    return secret_num


def guess(secret_num):
    different_num = []
    while len(different_num) != len(secret_num):
        user_num = input("Enter a number: ")
        if len(user_num) != len(secret_num):
            print("Your guess has to be 4 different digit numbers!")
            print("-" * 25)
        elif not user_num.isnumeric():
            print("Your guess has to be 4 different digit numbers!")
            print("-" * 25)
        else:
            for num in user_num:
                if num not in different_num:
                    different_num.append(num)
                else:
                    print("Your guess has to be 4 different digit numbers!")
                    print("-" * 25)
                    different_num.clear()
                    break
    return user_num


def counting(user_num, secret_num):
    bulls = 0
    cows = 0
    i = 0
    for num in user_num:
        if num == secret_num[i]:
            bulls += 1
            i += 1
        elif num in secret_num:
            cows += 1
            i += 1
        else:
            i += 1
    return bulls, cows


def finish(bulls, cows, secret_num, attempt):
    if bulls == len(secret_num):
        print(f"Correct, you've guessed the right number in {attempt} attempts.")
        if attempt in range(0, 5):
            print("WOW!!! How... How did you do that?!")
        elif attempt in range(5, 10):
            print("Not bad, not bad at all.")
        elif attempt in range(10, 15):
            print("Poor average.")
        elif attempt in range(15, 20):
            print("What a waste of time.")
        else:
            print("Just give up already...")
        exit()
    else:
        print(f"{bulls} bulls, {cows} cows")
        print("-" * 25)


main()
