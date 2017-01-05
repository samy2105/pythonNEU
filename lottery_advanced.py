import random


lottery_numbers = []


def main():

    print "Welcome to the Lottery numbers generator."
    numbers_count = int(raw_input("Please enter how many random numbers would you like to have (up to 10): "))

    numbers = random.sample(range(0,99), numbers_count)
    lottery_numbers.append(numbers)

    print "Try the game with these numbers: " + str(lottery_numbers)
    print "good luck and good bye"


if __name__ == "__main__":
    main()