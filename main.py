import random
from pathlib import Path

words = []

def get_word(mode):
	output = None
	while output == None:
		output = words[random.randint(0,len(words))]
		if mode:
			if len(output) < 8:
				output = None
		else:
			if len(output) < 6 or len(output) > 8:
				output = None
	return output

def mklist(word):
	output = []
	for letter in word:
		if letter not in output:
			output.append(letter)
	return output

with Path('words.txt').open() as file:
	for line in file:
		words.append(line)

while True:
	print('Guess the Mystery Word!')
	mode = input('Mode (Normal/Hard): ').lower().strip()
	if mode == '' or mode == 'n' or mode == 'normal':
		mode = False
	elif mode == 'h' or mode == 'hard':
		mode = True
	else:
		continue
	word = get_word(mode).strip().lower()
	inword = mklist(word)
	guessed = []
	wrongs = 0

	while True:
		for letter in word:
			print(letter if letter in guessed else '_', end=' ')
		print('')
		for letter in guessed:
			print(letter, end=' ')
		print('')
		print(8 - wrongs, 'guesses left')
		while True:
			guess = input('Guess: ').lower().strip()
			if len(guess) != 1:
				continue
			if not guess.isalpha():
				continue
			if guess in guessed:
				print(guess,'has already been guessed!')
				continue
			guessed.append(guess)
			if guess not in inword:
				wrongs += 1
			break
		allin = True
		for letter in inword:
			if letter not in guessed:
				allin = False
		if allin:
			print('***',word,'***')
			print('You guessed the word!')
			break
		if wrongs > 7:
			print('YOU LOSE!')
			print('The word was:',word)
			break

	if input('Continue (Y/N)? ').lower().strip() != 'y':
		break
