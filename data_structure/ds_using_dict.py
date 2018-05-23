addressbook = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", addressbook['Swaroop'])

del addressbook['Spammer']

print('\n there are {} contacts in the address-book \n' .format(len(addressbook)))

for name , address in addressbook.items():
        print("Contact {} at {}".format(name, address))

addressbook['Guido'] = 'guido@python.org'

if 'Guido' in addressbook:
    print("\n Guido's address is ", addressbook['Guido'])