# name_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]


# name = None
# while name != "Валера":
#     name = name_list.pop(0)

#     if name == "Валера":
#         print("Валера нашелся!")



# def find_person(name_input):
#     name = None
#     while name != name_input:
#         name = name_list.pop(0)
#         if name == name_input:
#             print('Этот человек нашелся')
#             break
#         if len(name_list) == 0:
#             print('Нет такого')
#             break



# find_person(input('Enter name : '))

# def ask_user():
#     while True:
#         user_in = input('Как дела? :')
#         if user_in == 'Хорошо':
#             print('Молодец!')
#             break


# ask_user()

# def get_answers(question):
#     answers = {'привет': 'И тебе привет!', 
#     'как дела': 'Лучше всех', 
#     'пока': 'увидимся'}
#     return answers.get(question.lower(), ' не знаю')



def get_answers(question):
    answers = {'какая погода': 'хорошая', 
               'как дела': 'Лучше всех', 
               'любимый цвет': 'синий'}
    
    return answers.get(question.lower(), ' не знаю')


def ask_user():

    while True:
        question = input('задай вопрос :')
        if question == 'пока':
            print('До встречи!')
            break
        print(get_answers(question))
try: 
    ask_user()
except KeyboardInterrupt:
    print('НЕ НАЖИМАЙ ctrl+C!')



