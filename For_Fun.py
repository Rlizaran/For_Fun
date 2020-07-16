""" def week(i):
    switcher = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday', 
    }
    return switcher.get(i, 'Invalid day of week') 
print(week(2))    """


""" type('177')
type(177)
print(type('177'))
print(type(177))
print(type(177.0)) """
# import random

# roll = random.randint(1, 100000)
# while True:
#     print(roll)
#     if roll == 10000 or roll == 7:
#         break
#     roll = random.randint(1, 100)

   
def check_for_fruit(A):
    found_fruit = []
    if 'apple' in A:
        found_fruit.append('apple')
    if 'peach' in A:
        found_fruit.append('peach')
    if 'blueberry' in A:
        found_fruit.append('blueberry')
        
    found_fruit_str = ''
    for fruit in found_fruit:
        found_fruit_str += fruit
        found_fruit_str += ', '
        
    if len(found_fruit) > 0:
        print(found_fruit_str + ' is found within the string')
    else:
        print('No fruit found in the string')
check_for_fruit('there are apples and peaches in this pie')