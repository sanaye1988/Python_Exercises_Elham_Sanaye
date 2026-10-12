data = [1, 2, 3]

try:
    user_index = int(input('enter your index:'))
    print(data[user_index])
except IndexError:
    raise IndexError('index mojood nist')
except ValueError:
    raise ValueError('faghat adad vared konid')