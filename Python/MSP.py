

stages = ['''
              0
              |
             /|\\
              |
             / \\ ''','''
              0
              |
             /|\\
              |
             /  ''','''

              0
              |
             /|\\
              |
                ''','''
              0
              |
             /|\\ ''','''
              0
              |
             /| ''','''

              0
              |
              | ''','''

              0
              | ''','''

              0 ''']


print(stages[0])
word_text = input("player 1 whats the word: ")
word = list(word_text.lower())
print(word)
print("\n"*100)
guess = "_" * len(word)
guess = list(guess)
guessed = False
won = True
tries = 0

while guess != word:
	letter = input("player 2 guess a letter: ")
	for i in range(len(word)):
		if word[i] == letter:
			guess[i] = letter
			guessed = True
			print(stages[tries])
			print(letter, "is in the word!")
			print(guess)
	if tries+1 < len(stages):
		if guessed == False:
			tries += 1
			print(stages[tries])
			print(letter, "not in word")
			print(guess)
	else:
		won = False
		break

	guessed = False

if won:
	print("congrats you win!")
else:
    	print("out of guesses")
