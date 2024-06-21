def hunger(Status):
    if Status == 0:
        return 'Im Hungry!!'
    elif Status ==1:
        return 'Im Okay!'
    else:
        return 'I want to go home!'

class placement:
    def __init__(self,level):
        if level==400:
            self.training = True
        else:
            self.training = False

    def department(self,department):
        if len(department) > 6: 
            return f'department is {self.training}'
        else:
            return 'Go home!'


    
x=int(input('Input Either 0 or 1 to determine your hunger status'))

print(hunger(x))

y=placement(500)
print(y.department('Biology'))

