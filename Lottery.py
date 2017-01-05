import random


lottery_numbers = []


def main():

    print "Welcome to the Lottery numbers generator."
    numbers_count = int(raw_input("Please enter how many random numbers would you like to have (up to 10): "))

    for i in range(0, numbers_count):
        random_num = random.randint(0, 99)
        lottery_numbers.append(random_num)

    print "Try the game with these numbers: " + str(lottery_numbers)
    print "good luck and good bye"


if __name__ == "__main__":
    main()
