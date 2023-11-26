import string
import random
import sys
import time
import shutil
import os
from pyfiglet import Figlet
from datetime import date

#config
characters = None
digits = None


#typewriter effect
def typewriter(t):
    columns = shutil.get_terminal_size().columns
    centered_text = t.center(columns)

    for characters in centered_text:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.01)

    sys.stdout.write('\n')  


# console stuff
os.system('cls')
os.system('mode con: cols=72 lines=29')
print(Figlet(font='slant').renderText('pw-generator'))

#config
typewriter('would you like to use characters In your passwords? (Y/N) \n')
characters = input('')

if characters == 'Y':
    characters = True
elif characters == 'N':
    characters = False
else:
    print('Invalid answer')
    
typewriter('would you like to use digits In your passwords? (Y/N) \n')
digits = input('')

if digits == 'Y':
    digits = True
elif digits == 'N':
    digits = False
else:
    print('Invalid answer')

typewriter('how long do you want your passwords to be?\n')
length = int(input())

typewriter('how many passwords do you want to generate?\n')
ammount = int(input())

os.system('cls')

def gen():
    global pw
    
    for _ in range(ammount):
        if characters and digits:
            pw = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
            print('\n')
            typewriter(pw)
        elif characters:
            pw = ''.join(random.choice(string.ascii_letters + string.punctuation) for _ in range(length))
            print('\n')
            typewriter(pw)
        elif digits:
            pw = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
            print('\n')
            typewriter(pw)

gen()

def save():
    global pw
    
    file_name = date.today().isoformat() + '.txt'

    with open(file_name, 'a') as f:
        for _ in range(ammount):
            if characters and digits:
                pw = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
                f.write(pw + '\n')
            elif characters:
                pw = ''.join(random.choice(string.ascii_letters + string.punctuation) for _ in range(length))
                f.write(pw + '\n')
            elif digits:
                pw = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
                f.write(pw + '\n')


print('\n')
typewriter('would you like to save these passwords to a file? (Y/N)')
save_option = input()

if save_option == 'Y':
    typewriter('okay, saving...')
    save()
    
elif save_option == 'N':
    typewriter('okay, quitting..')
    time.sleep(1)
    sys.exit()
else:
    print('Invalid answer')
