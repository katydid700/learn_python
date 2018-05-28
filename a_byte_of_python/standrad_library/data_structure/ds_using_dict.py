# coding=UTF-8
"""dict
将键与值联系到一起
键(key): 使用不可变的对象
值(value): 使用可变或不可变的对象
另外需要记住，字典中的成对的键值—值配对不会以任何方式进行排序。如果你希望为它们
安排一个特别的次序，只能在使用它们之前自行进行排序。
"""

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