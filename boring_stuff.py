from random import choice


number1 = int(input("Choose lower border: "))
number2 = int(input("Choose upper border: "))
number_pool=[]

def number_guessing(number1, number2):
    numbers = [n for n in range(number1, number2)]
    chosen_number = choice(numbers)
    print("Choosen number is", chosen_number)
    return chosen_number
    


def picking_number(number1, number2):
    numbers = [n for n in range(number1, number2)]
    my_number = choice(numbers)
    print(f"Your number is: {my_number}")
    return my_number


def checking_tickets(ticket1, ticket2):
    if ticket1 == ticket2:
        return False
    else:
        return True

plays = 0
game = True

while game:
    plays += 1
    picking_nums = number_guessing(number1, number2)
    picking_your_num = picking_number(number1, number2)
    game = checking_tickets(picking_nums, picking_your_num)
    
print("You Won! Lucky number is:", picking_your_num)
print(f"It took {plays} plays to win")
    