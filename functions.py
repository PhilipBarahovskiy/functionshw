'''
Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.
Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.
'''

print(
'''
Enter the command 'p' if you want to find out the name by the number;
Enter the command 's' if you want to find out the shelf by the doc. number;
Enter the command 'l' if you want to see list of all docs;
Enter the command 'a' if you want to add a document;
Enter the command 'd' if you want to delete a document from documents and directories;
Enter the command 'm' if you want to move a doc. number from one shelf to another;
Enter the command 'as' if you want add a shelf;
Enter the command 'q' if you want to log off.
''')

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def people():
  n = input('\tEnter the number: ')
  for doc in documents:
    if doc.get('number') != None and doc['number'] == n:
      return doc['name']
  print('Document does not exist.')
  return ''

def shelf():
  n = input('Enter the number: ')
  cur_shelf = ''
  for doc in documents:
    if doc.get('number') != None and doc['number'] == n:
      for shelf, list in directories.items():
        if n in list:
          cur_shelf = shelf
  return cur_shelf

def data_list():
  for doc in documents:
    print(f"{doc['type']} {doc['number']} {doc['name']}")
  return ''

def add():
  new_data = input('type, number, name, shelf: ').split()
  new_doc = {'type': new_data[0], 'number': new_data[1], 'name': new_data[2]}
  documents.append(new_doc)
  for shelf, list in directories.items():
    if new_data[-1] in shelf:
      list.append(new_data[1])
      return directories
  else:
    return ''


def add_shelf():
  shelf_num = input()
  if shelf_num not in directories.keys():
    directories[f'{shelf_num}'] = '[]'
    return directories
  else:
    return 'Shelf with this number exists'

def delete():
  n = input('Enter the number: ')
  i = 0
  while i < len(documents):
    for v in documents[i].values():
      if v == n:
        documents.pop(i)
    i += 1
  for v in directories.values():
    i = 0
    while i < len(v):
      if v[i] == n:
        v.pop(i)
      i += 1
  return directories

def move():
  n = input("Enter the number of document: ")
  new_shelf = input("Enter the new shelf number: ")
  if directories.get(new_shelf) == None:
    return ''
  for doc in documents:
    if doc.get('number') != None and doc['number'] == n:
      for shelf, list in directories.items():
        for el in list:
          if el == n:
            list.remove(el)
            directories[f'{new_shelf}'].append(f'{n}')
  return directories

while True:
  cmd = input('Enter the command [q, p, s, l, a, d, m, as]: ')
  if cmd == 'q':
    break
  elif cmd == 'p':
    print(people())
  elif cmd == 's':
    print(shelf())
  elif cmd == 'l':
    print(data_list())
  elif cmd == 'a':
    print(add())
  elif cmd == 'd':
    print(delete())
  elif cmd == 'm':
    print(move())
  elif cmd == 'as':
    print(add_shelf())
