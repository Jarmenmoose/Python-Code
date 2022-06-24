from random_word import RandomWords
r = RandomWords()
# Return a single random word
rand_word = r.get_random_word(hasDictionaryDef="true", minCorpusCount=100000)
#keeping track of correct & inccorect guesses
guessed = []
wrong = []
tries = 7

#looping until 7 tries
while tries>0:

#Printing the number of letters in word
    out = ""
    for letter in rand_word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + " _ "
    if out == rand_word:
        break

    #Getting user input
    print("Guess a letter in the word, then press enter:", out)
    print(tries,  "chances left")
    guess = input()

    #determining if in the random word or not
    if guess in guessed or guess in wrong:
        print("Already guessed", guess)
    elif guess in rand_word:
        print("Correct")
        guessed.append(guess)
    else:
        print("Nope")
        tries= tries - 1
        wrong.append(guess)
    print()

#If you win or lose
if tries:
    print("You guessed", rand_word)
else:
    print("You didn't get", rand_word)



#We used arrays for keeping track of correct & incorrect guesses
#We used the "in" function to determine whether or not the user input what in the random word
#We used randomword generator import tool
