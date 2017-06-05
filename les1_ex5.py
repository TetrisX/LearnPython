def get_answers(question):
    answers = {'какая погода': 'хорошая', 
               'как дела': 'Лучше всех', 
               'любимый цвет': 'синий'}
    try:
        return answers.get(question.lower(), ' не знаю')
    except (KeyboardInterrupt):
        return 'НЕ НАЖИМАЙ ctrl+C!'

print(get_answers(input('Вводи что то ')))