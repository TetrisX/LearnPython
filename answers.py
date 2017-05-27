def get_answers(question):
	answers = {'привет': 'И тебе привет!', 
	'как дела': 'Лучше всех', 
	'пока': 'увидимся'}
	return answers.get(question.lower(), ' не знаю')


print(get_answers('Привет'))

x = 0
while x < 10:
    print(x)
    x += 1