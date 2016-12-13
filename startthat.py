secret = 8
guess = int(raw_input("Let's play a game. What's the secret number?"
                  "Guess here: "))
right = "You are rich"
wrong = "We're sorry, we got your money :)"

if guess == secret:
    print right

else:
    print wrong