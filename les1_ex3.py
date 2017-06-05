school_score = [{'school_class': '8a', 'scores': [4,3,4,5,3]}, 
                {'school_class': '8б', 'scores': [4,4,4,5,4]}, 
                {'school_class': '8в', 'scores': [4,4,4,4,3]}, 
                {'school_class': '8г', 'scores': [4,4,4,4,4]}]

avg_sum = 0
for dic in school_score:
    s = sum(dic['scores']) / len(dic['scores'])
    avg_sum += s
    print (dic['school_class'], s)
    print (len((dic['scores'])))

a = len(school_score)
print(a)
k = avg_sum / a
print ('Средний балл', k)

