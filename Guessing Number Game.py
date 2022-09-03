#!/usr/bin/env python
# coding: utf-8

# In[11]:


game_instr = 'Game Instructions'

print(game_instr.center(72, '*'))
print('1. Please read the instructions carefully')
print('2. You have to guess number between 1 and 10')
print('3. You have 10 chance to guess the number')
print("4. If you didn't guess the number in first 3 chance, then you will get a hint to guess the number")
print("5. If you run out of 10 chance, then your game will be end there")
print('''

''')

import random

num = random.randint(1, 10)

guesses = [0]

while True:
    guess = int(input('Pick a number between 1 and 10 \nWhat is your guess? :'))
    
    
    if guess < 1 or guess > 10:
        print('Warning: 🚨 Please choose number between 1 and 10 🚨')
        continue
    
    if guess == num:
        print(f'🏆 Congratulations you won 🏆')
        print(f'You took {len(guesses)} chance to guess the right number')
        break
    else:
        print('❌ Wrong Guess ❌, Please Try Again')
    
    if len(guesses) in range(4, 10):
        if guess < num:
            print('Hint: Too Low ⏬')
        else:
            print('Hint: Too High ⏫')
    else:
        pass
       
    if len(guesses) == 10:
        print('Oops, Your chances are over')
        break
    else:
        pass
    
    guesses.append(guess)


# In[ ]:




