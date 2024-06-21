def hunger(Status):
    if Status == 0:
        return 'Im Hungry!!'
    else:
        return 'Im Okay!'
    
x=int(input('Input Either 0 or 1 to determine your hunger status'))

print(hunger(x))
