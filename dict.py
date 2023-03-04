names = ['yongma', 'lushu', 'guge', 'anzhua']
user = ['user1', 'user2', 'user3', 'user4']

to_dict = {}

for key, value in zip(names, user):
    to_dict[key] = value

print(to_dict)
to_dict2 = {
    key: value for (key, value) in zip(names, user)
}
print(to_dict2)
to_dict3 = {
    user[i]: names[i] for i in range(len(names))
}
print(to_dict3)

print('\n = = = = = = = = = = =dict= = = = = = = = = = = \n')

#dictionary = {key: expression for (key,value) in iterable}
#dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}

weather = {'manila': 'sunny', 'jakarta': 'rainy', 'cavite': 'rainy'}

get_sunny = {k: v for (k, v) in weather.items() if v == 'sunny'}
get_rainy = {k: v for (k, v) in weather.items() if v == 'rainy'}

print(get_sunny, '\n', get_rainy)

weather2 = {'manila': 39, 'jakarta': 30, 'cavite': 35}
get_warm_cold = {k: ('warm' if v >= 35 else 'cold')
                 for (k, v) in weather2.items()}

print(weather2)
print(get_warm_cold)
