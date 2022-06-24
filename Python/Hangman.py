import random
from random_word import RandomWords
x = True
r = RandomWords()
count = 0
j = 0

while x:
    ToPlay = input ("Want to play Hangman?\n\n")
    if ToPlay ==("Yes" or "yes"):

        R_Word = r.get_random_word(hasDictionaryDef="true",includePartOfSpeech="True",minCorpusCount=10000)
        WordArray = list (R_Word)
        print (R_Word)
        N_Tot_Let = len(WordArray)
        N_Rem_Let = N_Tot_Let
        N_Lives = 5
        while count < N_Tot_Let:
            print ("_")
            count+= 1



        while N_Rem_Let> 0 and N_Lives> 0:
            Correct = []
            Guess = input ("\nGuess a letter:\n\n")
            while j < N_Tot_Let: #looking at single letter
                if Guess == WordArray[j]:
                    print (WordArray[j])
                    N_Rem_Let-=1
                    Correct.append(Guess)
                elif Correct == WordArray[j]:
                    print (WordArray[j])
                elif Guess != WordArray[j]:
                    print ("_")
                print(N_Lives, N_Rem_Let, Correct)
                j+=1

            j=0
        if N_Rem_Let == 0:
            print("You Win")
        elif N_Lives == 0:
            print("Off to the Gallows")

    elif ToPlay !=("No" or "no"):
        x = False
