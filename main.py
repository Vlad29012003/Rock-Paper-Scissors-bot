# from random import choice 

# variant = {
#     1:' камень',
#     2:'ножницы',
#     3:'бумага'}

# def variant_game(user_choice :int ):
#     computer_choice = choice (list(variant))
#     if user_choice == computer_choice:
#         return f'ничия, чувак выбрал {variant [computer_choice]}'

#     elif  user_choice == 1 and computer_choice==2 \
#         or user_choice ==2 and computer_choice == 3 \
#             or user_choice == 3 and computer_choice == 1:
#         return f'чувак ты побелил.бот выбрал {variant[computer_choice]}' 

#     elif  user_choice == 1 and computer_choice==3 \
#         or user_choice ==2 and computer_choice == 1 \
#             or user_choice == 3 and computer_choice == 2:
#         return f'чувак ты проиграл .бот выбрал {variant[computer_choice]}' 


#     else:
#         return 'выберите корректный ответб не тупите мистер'

# def stiker(result:int):
#     pass

from random import choice

variant = {
    1:'камень',
    2:'ножницы',
    3:'бумага'
}

def variant_game(user_choice:int):
    computer_choice = choice(list(variant))
    if user_choice == computer_choice:
        return f'ничья чувак выбрал {variant[computer_choice]}'

    elif user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice == 3 or user_choice == 3 and computer_choice == 1:
        return f'чувак ты победил, бот выбрал {variant[computer_choice]}'

    
    elif user_choice == 1 and computer_choice == 3 or user_choice == 2 and computer_choice == 1 or user_choice == 3 and computer_choice == 2:
        return f'чувак ты прoиграл, бот выбрал {variant[computer_choice]}'

    else:
        return 'выборите корректный ответ'
    
def sticker(result:int):
    pass