import random
word_list=['apple','mango','fig','grapes','kiwi']

def get_random_word():
  return random.choice([word for word in word_list if len(word)<=6])

def hangman():
  word=get_random_word()
  guessed_word=['_']*len(word)
  guessed_letters=[]
  attempts=6
  print("Welcome to hangman")

  while attempts>0:
    print(f"Word:{' '.join(guessed_word)}")
    print(f"You guessed: {', '.join(guessed_letters)}")
    print(f"Attempts: {attempts}")
    
    guess=input("Guess a letter:").lower()

    if guess in guessed_letters:
      print("You already guessed this letter")
      continue
    elif guess in word:
      for i in range(len(word)):
        if word[i]==guess:
          guessed_word[i]=guess
      print("Good guess")
    else:
      attempts=attempts-1
      print("Wrong guess")
    guessed_letters.append(guess)
    if '_' not in guessed_word:
      print(f"Congrats you won the game.The word is {word}")
      break
  else:
    p
