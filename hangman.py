import random
import os

# reading data
def read_data():
    words = []
    with open('./data.txt', 'r', encoding='utf-8') as d:
        for line in d:
            words.append(line.strip().upper())
    return words


# variables
def run():
    data = read_data()
    word = random.choice(data)
    word_list = [letter for letter in word]
    word_underscores = "_" * len(word_list)
    used_letters = []
   
    #loop
    while len(word_list) > 0:

        os.system('cls')
        print('☹☹☹☹☹☹☹☹☹☹☹☹☹☹☹☹☹☹☹☹☹☹')
        print('Welcome to Hangman Game, guess the word... ')
        current_word = [letter if letter in used_letters else '_' for letter in word]
        print(current_word)
        print(' ')
        print('You have used these letters: ', used_letters)  
        print(' ')
        user_letter = input('Type a letter: ').upper()


        if user_letter.isalpha():

            if user_letter in word_list:
                word_list.remove(user_letter)

            if user_letter in used_letters:
                print('You have already use that letter')

            if user_letter not in used_letters:
                used_letters.append(user_letter)

               
        else:
            print('Type a letter, please. ')
            

    if len(word_list) == 0:
        print(' ')
        print('You win this time!, your word is: ', word)
        print(' ')
        print('Game by: Carlos Rojas Bate')
        print('https://www.linkedin.com/in/carlos-rojas-bate-053358246/')
        print('https://github.com/carlosbate')



    

if __name__ == '__main__':
    run()