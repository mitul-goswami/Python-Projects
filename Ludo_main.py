import random

sum1=0
sum2=0
for i in range (1,10000000000):
    dice1=random.randint(1,6)
    roll1=input(print('Player 1 Roll The Dice'))
    if roll1=='roll':
        print('The Dice Came %d'%dice1)
    else:
        print('INVALID ENTRY')
        exit()
    dice2=random.randint(1,6)
    roll2=input(print('                         Player 2 Roll The Dice'))
    if roll2=='roll':
         print('                                The Dice Came %d'%dice2)
    else:
        print('INVALID ENTRY')
        exit()
    if dice1==6 or dice1==5 or dice1==4 or dice1==3 or dice1==2 or dice1==1:
       sum1+=dice1
       print('Player 1 Position Is %d'%sum1)
       if sum1>=52:
            print('PLAYER 1 WON !!')
            exit()
    elif dice2==6 or dice2==5 or dice2==4 or dice2==3 or dice2==2 or dice2==1:
        sum2+=dice2
        print('                                 Player 2 Position Is %d'%sum2)
        if sum2>=52:
            print('                             PLAYER 2 WON !!')
            exit()
