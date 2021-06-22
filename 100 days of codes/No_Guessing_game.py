import random
number = random.randint(0, 100)

while True:
    no = int(input("what is your guess: "))
    if no > number:
        print(f"Your guess of {no} is too high!")
    elif no < number:
        print(f"Your guess of {no} is too low")
    elif no == number:
        print(f"Just right! the answer is {no}")
        break

