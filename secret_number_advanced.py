import random


def main():


    random_num = random.randint(0, 99)
    # das ist eine fore-schleife
    for i in range(5):
        secret = random_num
        guess = int(raw_input("wie lautet die geheimzahl? (zwischen 0 und 100 - du hast 5 Versuche):"))

        if guess == secret:
            print "treffer!"
            break
        if i == 4:
            print "game over"
            break
        elif guess > secret:
            print "sie ist niedriger"
        elif guess < secret:
            print "sie ist hoeher"


if __name__ == "__main__":
    main()