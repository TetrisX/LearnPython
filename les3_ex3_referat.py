sum_word = 0

with open('referat.txt', 'r', encoding='utf-8') as var_1:
    for line in var_1:
        word = line.split(' ')
        sum_word = sum_word + len(word)

print(sum_word)




