my_dict = {'Elena': 2001, 'Sasha': 2002, 'Alice': 2003}
print(my_dict)
print(my_dict.get('Alice'))
print(my_dict.get('Denis'))
my_dict['Kamila'] = 2000
my_dict['Ross'] = 1968
a = my_dict.pop('Ross')
print(a)
print(my_dict)
#Работа с множеством
my_set = {1, 3, 1, 4, 2, 3, 4, 'string', True, 'string'}
print(my_set)
my_set.add(5)
my_set.add('Joseph')
print(my_set)
my_set.discard('string')
print(my_set)




