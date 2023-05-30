import random
rand=random.randint(1,3)
if rand==1:
    comp='STONE'
elif rand==2:
    comp='PAPER'
elif rand==3:
    comp='SCISSOR'
print('Computer Played')
player=input("Player Turn: STONE PAPER OR SCISSOR ??\n")
if player=='STONE'or player=='PAPER'or player=='SCISSOR':
    pass
else:
    exit()
def game(comp,player):
    if  comp=='STONE':
        if player=='PAPER':
            return True
        elif player=='SCISSOR':
            return False
        elif player=='STONE':
            return None
    if comp=='PAPER':
         if player=='STONE':
            return False
         elif player=='SCISSOR':
            return True
         elif player=='PAPER':
            return None
    if comp=='SCISSOR':
         if player=='PAPER':
            return False
         elif player=='STONE':
            return True
         elif player=='SCISSOR':
            return None
print('Computer Played %s'%comp)
print('You Played %s'%player)
winner=game(comp,player)
if winner==None:
    print('The Game Is Tied!')
elif winner==True:
    print('You WON!!')
elif winner==False:
    print('Computer WON!! You Lost!!')

