cityName = ['Detroit', 'Ann Arbor', 'Pittsburg', 'Mars', 'New York']
populations = [680250, 117070, 304391, 1683, 8406000]
states = ['MI', 'MI', 'PA', 'PA', 'NY']

city_tuples = zip(cityName, populations, states)




cities = []
for city_tup in city_tuples:
    name, pop, state = city_tup
    print(city_tup)
    print(name, pop, state)
    print('---')
