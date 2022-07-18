import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["souris", "chien", "elephant", "jouet", "Balai", "Banjo", "Barbe", "Bonne", "Bruit", "Buche", "Carte", "Gifle"]
lives=3

while(lives>0):
    chosen_word= random.choice(word_list)
    chosen_display=[]
    guessed_letters=[]
    for _ in range(len(chosen_word)):
        chosen_display.append("_")

    end_of_game=False
    round=len(stages)-1

    while(chosen_display.count("_")!=0 and not end_of_game):
        print(chosen_display)
        guess_letter = (input("Choisissez une lettre: ? ")).lower()
        guessed_count=guessed_letters.count(guess_letter)
        if(guessed_count!=0):
            print(f"Tu as déjà demandé cette lettre : {guessed_letters}")
        else:
            guessed_letters.append(guess_letter)
            letter_count = chosen_word.count(guess_letter)
            if letter_count>0:
                for position in range(len(chosen_word)):
                    if guess_letter==chosen_word[position]:
                        chosen_display[position]=guess_letter
            else:
                print(stages[round])
                round-=1
            if(round<0):
                end_of_game=True
            if(chosen_display.count("_")==0):
                print(chosen_word)
            
    if(end_of_game):
        print("Pendu !! Pendu !!")
        lives-=1
    if (chosen_display.count("_")==0):
        print("Bien joué, vous avez deviné !!")
    if(lives<=0):
        print("Plus de vie, fin de partie")
    else:
        print("Partie suivante \n")
        end_of_game=False
        round=len(stages)-1


