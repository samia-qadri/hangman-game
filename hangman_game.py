""" This is me Samia Qadri - student of Software Engineering (BSSE),UBIT,KU.
    I am also enrolled in side-course AI and Data Science, SMIT.
    This is a hangman game , as part of my practice work.
    LinkedIn: Samia Qadri """

# this list is used to show hangman visuals on wrong guess
hangman_stages = [
    """
       -----            
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


import random
 # it is list of words that code will use .
words=["honest","scientific","python","software","pandas",
       "science","apple","computer","table","book","programming",
       "clothes","water","football","light","intelligent","internet",
       "screen","author","student","engineer","dinner","breakfast",
       "library","chocolate","friendship","triangle","mirror"]

 # It greets user and tell instructions.
print("\n WELCOME TO HANGMAN GAME !")
print(" > you have to guess a word by one letter at a time. ")
print(" > You have six lives\n     incorrect guess will deduct the life")
print("Let's start")
try:
    play=True
    while(play==True):
        random_choice=(random.choice(words)).lower()
        for i in range (1,len(random_choice)+1):
            print(" _ ",end='')
        times= 6
        found = False
        user_guess=""
        print("")
        guessed_words=""
        
 # as there are 6 lives, so I've initialized a variable; time=6, then while loop works till it is greater than 0.
 # Inside the loop, code checks if answer is correct or not, then deduct life incase of wrong answer
 
        while(times>0):
            print("")
            user_word=input("> Enter a letter: ").lower()
            if (len(user_word)==1 and (user_word >= 'a' and user_word <='z')):
                if(user_word not in guessed_words):
                    guessed_words+=user_word +" "
                    if(user_word in random_choice):
                        print("Correct guess! ")        
                        user_guess+=user_word
                    else: 
                        times-=1
                        print("Wrong guess! lives-1")
                        print("Remaining lives: ",times)
                        print(hangman_stages[6 - times])

                    # this will show the letters in words, guessed by user     
                    show=""
                    for value in random_choice:
                        if value in user_guess:
                                show+=value+" "
                        else:
                                show+=" _ "
                    print(" word: ",show)
                    
                    if set(random_choice).issubset(set(user_guess)):
                            print("congratulations! you won ")
                            found=True
                            break
                #in case of duplicate letter entry, message will be displayed
                else:
                    print("duplicate letter!")
                print(" guessed words are as : ",guessed_words," ")
            elif(user_word == '' or len(user_word)!=1):
                print("invalid character entered! ")      
            else:
                print("invalid character entered! ")
                
        if not found:
            print("You lose the game. ")
            
        # this will ask user if one wants to play again     
        again=input("Do you want to try again? yes/no ").lower()
        if (again.lower()=="yes"):
            play=True
        elif (again.lower()=="no"):
            play= False
        else:
            print("Invalid! Game stopped.")
            play=False
            
except Exception as e:
    print(e)
