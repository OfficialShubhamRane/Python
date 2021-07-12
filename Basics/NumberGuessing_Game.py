secretNumber = 9
guessLimit = 3;
guessAttempted = 0;

while guessAttempted < guessLimit:
    guessedValue = input( f"Guess attempt no. {guessAttempted+1}: " );

    if int(guessedValue) == secretNumber:
        print("Congrats! You have Won.");
        break;
    guessAttempted += 1;

# Intresting !!!!!!!!!!
else:
    print("Failed!");