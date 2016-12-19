x = int(raw_input("Select a number between 1 and 100: "))

for x in range(1, x + 1):

    if x % 3 == 0 and x % 5 == 0:
        print "fizzbuzz"

    elif x % 3 == 0:
        print "fizz"

    elif x % 5 == 0:
        print "buzz"

    else:
        print x
