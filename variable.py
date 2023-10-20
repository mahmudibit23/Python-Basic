# this is variable section for practice



# message = 'Hello world'
# print(message)

# This is string section

# name = 'Mahmud'
# message = f'Hello {name} how r you '
# print(message)

#This is the string length

# str = "My Name is Mahmud Islam"
# str_len = len(str)
# print(str_len)

#Python user input function

# name = input('Enter the full name: ')
# print(name)

# price = input('Enter the price ($):')
# tax = input('Enter the tax rate (%):')
#
# net_price = price * tax / 100
#
# print(f'The net price is ${net_price}')

price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

net_price = int(price) * int(tax) / 100
print(f'The net price is ${net_price}')