from random import randint

print('[1] Stone')
print('[2] Paper')
print('[3] Scissor')

rounds = 1
for a in range(5):
    com = randint(1,3)
    print ('Round: ', rounds)
    rounds = rounds + 1
    user = eval(input('User: '))
    print ('Computer:', com)

    if user == 1 and com == 1:
        print ('Winner: Draw')
    elif user == 2 and com ==2:
        print ('Winner: Draw')
    elif user == 3 and com == 3:
        print ('Winner: Draw')
    elif user == 1 and com == 2:
        print ('Winner: Computer')
    elif user == 1 and com == 3:
        print ('Winner: User')
    elif user == 2 and com == 1:
        print ('Winner: User')
    elif user == 2 and com == 3:
        print ('Winner: Computer')
    elif user == 3 and com == 1:
        print ('Winner: Computer')
    elif user == 3 and com == 2:
        print ('Winner: Computer')
        
    else:
        print('Invalid')

    print('\n')