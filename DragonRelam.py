import random
import time

def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = raw_input()
        return cave

def checkCave(chooseCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    #print friendlyCave
    #print 'chooseCave', chooseCave()
    if chooseCave == friendlyCave:
         print('Gives you his treasure!')
    else:
         print('Gobbles you down in one bite!')     
    print('Do you want to play again? (yes or no)')
    playAgain =raw_input()
    while (playAgain == 'yes') or (playAgain == 'y'):
        
        displayIntro()

        caveNumber = chooseCave()
        
        checkCave(caveNumber)

    
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

        displayIntro()
        caveNumber=0
        caveNumber = chooseCave()
        
        checkCave(caveNumber)
