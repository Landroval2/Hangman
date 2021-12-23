import random
import os

FILE_PATH = './archivos/data.txt'


def get_words_from_file(text_file):
    word_list = []
    with open(text_file, 'r', encoding='utf-8') as f:
        for word in f:
            word_list.append(word)
    return word_list


class Hangman():
    def __init__(self):
        self.words = get_words_from_file(FILE_PATH)


class Game(Hangman):

    def __init__(self):
        super().__init__()
        self.word = random.choice(self.words)
        self.letters = []
        self.correct_letters = []
        self.attempts = 0
    
    def start_game(self):
        print('Guess the word: ')
        print()
        print('- ' * len(self.word))
        print()
        while self.attempts < 6:
            print('Guess the word: ')
            print()
            self.update_screen()
        if self.attempts == 6:
            print(f'You have lost the game. The word was: {self.word}')
        elif len(self.correct_letters) == len(self.word):
            print(f'Congratulations! You have guessed the word: {self.word}')
    def make_a_move(self):
        letter = input("Please enter a letter: ")
        while True:
            if letter in self.letters:
                letter = input("Please enter a different letter: ")
            elif not letter.isalpha():
                letter = input("Please enter a valid character: ")
            elif (len(letter) == 1):
                self.letters.append(letter)
                if letter in self.word:
                    self.correct_letters.append(letter)
                else:
                    self.attempts += 1
                break
        

    def update_screen(self):
        self.make_a_move()
        for letter in self.word:
            if letter in self.correct_letters:
                print(letter, end='')
            else:
                print("_", end='')
        print()