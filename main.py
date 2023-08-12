import re
import csv
from pprint import pprint

def last_first_sur_name(contacts_list):
    for contact in contacts_list:
        contact[0] = ' '.join(contact[0:3])
    pattern = r"\w+"
    # name_list = []
    for contact in contacts_list:
        name_list = re.findall(pattern, contact[0])
        contact[0] = name_list[0]
        if len(name_list) > 1:
            contact[1] = name_list[1]
            if len(name_list) > 2:
                contact[2] = name_list[2]
    return(contacts_list)


# +7(999)999-99-99 доб.9999
def phone(contacts_list):
    for contact in contacts_list:
        if contact[5] !='' and contact[5] !='phone':
            pattern = r"\W"
            contact[5] = re.sub(pattern, '', contact[5])
            pattern = r"доб"
            f = re.search(pattern, contact[5])
            if f is None:
                contact[5] = '+7(' + contact[5][1:4] + ')' + contact[5][4:7] + '-' + contact[5][7:9] + '-' + contact[5][9:]
            else:
                contact[5] = '+7(' + contact[5][1:4] + ')' + contact[5][4:7] + '-' + contact[5][7:9] + '-' + contact[5][9:11] + ' доб.' + contact[5][14:]
    return (contacts_list)


def duplicates(contacts_list):
    del_index = []
    for i, contact in enumerate(contacts_list):
        for j in range(i+1,len(contacts_list)):
            if contact[0] == contacts_list[j][0] and contact[1] == contacts_list[j][1] and (contact[3] == contacts_list[j][3] or contact[3] == '' or  contacts_list[j][3] == ''):
                for f in range(7):
                    if contact[f] != contacts_list[j][f]:
                        contact[f] = contact[f] + ' ' + contacts_list[j][f]
                contacts_list[j] = 'for del'
    i = 0
    while i < len(contacts_list):
        if contacts_list[i] == 'for del':
            contacts_list.pop(i)
        i+=1
    return (contacts_list)


with open("phonebook_raw.csv", encoding="utf8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
## 1. Выполните пункты 1-3 задания.
contacts_list = last_first_sur_name(contacts_list)
contacts_list = phone(contacts_list)
contacts_list = duplicates(contacts_list)
pprint(contacts_list)
## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w",encoding="utf8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)