import random
comp= random.randint(1,6)
sum=0
for i in range (1,100000):
    runs=int(input('Enter Your Runs : '))
    if runs>6 or runs<1:
        print('INVALID ENTRY')
        exit()
    if runs!=comp:
        print('%d RUNS!!'%runs)  
        sum+=runs
    elif runs==comp:
        print('Computer Gave %d'%comp)
        print('Oops OUT!!')
        print('Total Runs Scored =  %d'%sum)
        exit()

