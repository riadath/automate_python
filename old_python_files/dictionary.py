states = {
    'Sylhet': 'SYL',
    'Dhaka': 'DHK',
    'Rajshahi': 'RJS',
    'Khulna': 'KLN',
    'Chittagong': 'CTG'
}

cities = {
    'SYL': 'Amborkhana',
    'DHK': 'Zindabazar',
    'RJS': 'Chowhatta',
    'KLN': 'Akhali',
    'CTG': 'Khilgao'
}


print('_' * 10)
print("SYL state has: ", cities['SYL'])
print('DHK state has ', cities['CTG'])

print('-' * 10)
print("Sylhet's abbreviation is ", states['Sylhet'])
print("Chittagong's abbreviation is ", states['Chittagong'])

print('-' * 10)
for state, abr in list(states.items()):
    print(f"{state} is abbreviated as {abr}")

print('_' * 20)
for city, abvr in list(cities.items()):
    print(f"{city} is abbreviated as {abvr}")

print('-' * 10)
state = states.get('Rangpur')
if not state:
    print("The state is not listed")

city = cities.get('SYL', 'Not listed')
print(f"The city for the state 'SYL' is : {city}")

