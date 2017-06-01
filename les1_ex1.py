age = int(input ('Сколько вам лет? :'))


if age < 7:
    print ('Вы ходите в детский сад.')
elif 7<= age <=18:
    print ('Вы учитесь в школе.')
elif 19<= age <=25:
    print ('Вы учитесь в ВУЗе.')
elif age >18:
    print ('Вы работаете.')