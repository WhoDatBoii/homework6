my_dict = {'Alex': 2001, 'Vasya': 2000, 'Dasha': 1999}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Dasha'])
print('Not existing value: ', my_dict.get('Sasha'))
a = my_dict.pop('Alex')
print('Deleted value: ', a)
my_dict.update({'Anton': 1998,
                'Inna': 1999})
print('Modified dictionary: ', my_dict)

my_set = {1, 'Апельсин', 1, 3, 3.141, 1, 3, (1, 2, 3)}
print('Set: ', my_set)
my_set.add(5)
my_set.add(7)
my_set.discard(3.141)
print('Modified set: ', my_set)
