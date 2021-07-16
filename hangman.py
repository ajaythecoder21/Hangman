# -*- coding: utf-8 -*-

letters = ['i', 'n', 'd', 'i', 'a', 'n']
spaces = len(letters)
if spaces != 0:
    guessed_letter = input('Please enter a letter')
for i in range(len(letters)):
    if guessed_letter in letters:
        if guessed_letter == 'i' or guessed_letter == 'n':
            spaces -= 2
            if guessed_letter == 'i':
                letters.remove(guessed_letter)
                letters.remove(guessed_letter)
                if spaces != 0:
                    guessed_letter = input('Please enter a letter')
                else:
                    print('You Win!!!')
            elif guessed_letter == 'n':
                letters.remove(guessed_letter)
                letters.remove(guessed_letter)
                if spaces != 0:
                    guessed_letter = input('Please enter a letter')
                else:
                    print('You Win!!!')
        elif guessed_letter == 'd' or guessed_letter == 'a':
            spaces -= 1
            if guessed_letter == 'd':
                letters.remove(guessed_letter)
                if spaces != 0:
                    guessed_letter = input('Please enter a letter')
                else:
                    print('You Win!!!')
            elif guessed_letter == 'a':
                letters.remove(guessed_letter)
                if spaces != 0:
                    guessed_letter = input('Please enter a letter')
                else:
                    print('You Win!!!')
            

        

        
        