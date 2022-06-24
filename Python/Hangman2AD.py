import random
from random_word import RandomWords
x = True
r = RandomWords()
R_Word = r.get_random_word(hasDictionaryDef="true",includePartOfSpeech="True",minCorpusCount=10000).lower()
print (R_Word)
WordArray =list (R_Word)


#Storing Guesses
Correct = []
Incorrect = []

Fail = 0
while Fail < 5:
    j=0
    print (WordArray)



#Guess
    Guess = input ("Guess a letter\n\n")

#Letter Check
    if Guess in Correct or Guess in Incorrect:
        print ("Try another letter")
    elif Guess in R_Word:
        print ("Correct")
        Correct.append(Guess)
    else:
        print ("incorrect")
        Incorrect.append(Guess)
        Fail+=1

#Writing word
#Sticking Point*****
    while j < len(R_Word):
        if WordArray[j] in Correct:
            print (WordArray[j])
#******            
        else:
            print ("_")
        #print(WordArray[j])
        j+=1
    if len(Correct) == len(R_Word):
        print("You win")
    if Fail == 5:
        print("You lose")
