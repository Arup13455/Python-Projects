import random

def hangman():
    word_list = ['python', 'java', 'ruby', 'javascript', 'html', 'css']
    chosen_word = random.choice(word_list)
    guessed_letters = []
    tries = 7

    # Loop until the player wins or loses
    while tries > 0:
        guessed_word = ''
        for letter in chosen_word:
            if letter in guessed_letters:
                guessed_word += letter + ' '
            else:
                guessed_word += '_ '

        print('Guessed word:', guessed_word)

        if '_' not in guessed_word:
            print('Congratulations! You won!')
            break

        guess = input('Guess a letter: ').lower()

        if guess in guessed_letters:
            print('You already guessed that letter. Try again.')
            continue

        guessed_letters.append(guess)

        if guess not in chosen_word:
            tries -= 1
            print('Wrong guess. Tries left:', tries)

        print_hangman(tries)

    if tries == 0:
        print('You lost! The word was:', chosen_word)

def print_hangman(tries):
    stages = [
        '''
           _______
           |     |
           |     O
           |    \\|/
           |     |
           |    / \\
           -
        ''',
        '''
           _______
           |     |
           |     O
           |    \\|/
           |     |
           |    /
           -
        ''',
        '''
           _______
           |     |
           |     O
           |    \\|/
           |     |
           |
           -
        ''',
        '''
           _______
           |     |
           |     O
           |    \\|
           |     |
           |
           -
        ''',
        '''
           _______
           |     |
           |     O
           |     |
           |     |
           |
           -
        ''',
        '''
           _______
           |     |
           |     O
           |
           |
           |
           -
        ''',
        '''
           _______
           |     |
           |
           |
           |
           |
           -
        ''',
        '''
           _______
           |     
           |
           |
           |
           |
           -
        '''
    ]
    print(stages[tries])

hangman()