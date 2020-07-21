A = 'apples'
B='appricots'

print('A ord: B ord')
for a_char, b_char in zip(A, B):
    print(f'{ord(a_char):<6}: {ord(b_char):>}')

