def hunger(Status):
    if Status == 0:
        return 'Im Hungry!!'
    elif Status ==1:
        return 'Im Okay!'
    else:
        return 'I want to go home!'
    
x=int(input('Input Either 0 or 1 to determine your hunger status'))

print(hunger(x))


