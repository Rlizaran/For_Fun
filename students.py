students = ['James', 'Draepper', 'Tatiana']

def append_name_to_list(my_list):
    while True:
        inp = input('Enter name: ')
        if inp == 'done':
            break
        name = str(inp)
        my_list.append(name)


append_name_to_list(students)
print(students)