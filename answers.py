def get_answers(question):
    answers = {'привет': 'И тебе привет!', 
    'как дела': 'Лучше всех', 
    'пока': 'увидимся'}
    return answers.get(question.lower(), ' не знаю')

if __name__ == '__main__':
    print(get_answers(input('Задавай свои вопросики: ')))

# x = 0
# while x < 10:
#     print(x)
#     x += 1