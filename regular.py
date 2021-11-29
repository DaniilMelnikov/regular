import re

from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)  

for index, list in enumerate(contacts_list[1:]):
    if len(re.findall("\w+", list[0])) == 3:
        write_list = re.findall("\w+", list[0])
        for id, el in enumerate(write_list):
            contacts_list[index + 1][id] = el
    elif len(re.findall("\w+", list[0])) == 2:
        contacts_list[index + 1][2] = contacts_list[index + 1][1]
        write_list = re.findall("\w+", list[0])
        for id, el in enumerate(write_list):
            contacts_list[index + 1][id] = el
    elif len(re.findall("\w+", list[0])) == 1:
        write_list = re.findall("\w+", list[1])
        for id, el in enumerate(write_list):
            contacts_list[index + 1][id + 1] = el
    overwriting_phone = re.sub(r"(\+7|8)?\s*\(*(\d{3})\)*\s*\-*(\d{3})\-*(\d{2})\-*(\d{2})(\s*)\(*(\д*\о*\б*\.*)\s*(\d+)*\)*", "+7(\\2)\\3-\\4-\\5\\6\\7\\8", list[5])
    contacts_list[index + 1][5] = overwriting_phone         

for index, list in enumerate(contacts_list[1:]):
    name = list[0]
    int_name = 0
    for ind, list in enumerate(contacts_list[1:]):
        double_name = list[0]
        if name == double_name:
            int_name += 1
            if int_name == 2:
                for id, el in enumerate(list[3:]):
                    if el == '':
                        pass
                    else:
                        contacts_list[index][id + 3] = el
                    if id == 3:
                        del contacts_list[ind + 1]
    new_contact_list = contacts_list

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contact_list)