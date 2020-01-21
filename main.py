import random
import datetime
names = 'Никита Елена Дмитрий Владимир Ольга Иннокентий Максим Василий Николай Анастасия \
Наталья Игорь Антон Роман Юрий Марья Елизавета Оксана Виталий Дарья'
names = names.split()

def choice(list, N):
    if N<1:
        pass
    else:
        return random.choice(list) + ' ' + str(choice(list, N-1))

print(choice(names,20))

def most_common(names_list):
    names_list = names_list.split()
    names_dict = {}
    for name in names_list:
        if name in names_dict.keys():
            names_dict[name] += 1
        else:
            names_dict[name] = 1
    top = list(names_dict.items())
    top.sort(key=lambda i: i[1], reverse=True)
    return top[:1]
print(most_common(choice(names,20)))

def most_common_letter(names_list):
    names_list = names_list.split()
    letter_dict = {}
    for name in names_list:
        if name[0:1] in letter_dict.keys():
            letter_dict[name[0:1]] += 1
        else:
            letter_dict[name[0:1]] = 1
    top = list(letter_dict.items())
    top.sort(key=lambda i: i[1], reverse=False)
    return top[:1]
print(most_common_letter(choice(names,20)))

with open('log.txt') as f:
    logs = f.readlines()
    all_dates = list(map(lambda x:x.split(',')[0],logs))
    all_dates.sort(key = lambda i:datetime.datetime.strptime(i, '%Y-%m-%d %H:%M:%S'), reverse = True)
print(all_dates[0])

