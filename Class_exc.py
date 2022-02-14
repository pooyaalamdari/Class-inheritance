cityName = ['Detroit', 'Ann Arbor', 'Pittsburg', 'Mars', 'New York']
populations = [680250, 117070, 304391, 1683, 8406000]
states = ['MI', 'MI', 'PA', 'PA', 'NY']

city_tuples = zip(cityName, populations, states)

class City:
    def __init__(self, n, p, s):
        self.name = n
        self.population = p
        self.state = s
    def __str__(self):
        return f'city name: {self.name}, state name: {self.state}, pop: {self.population}'


cities = []
for city_tup in city_tuples:
    name, pop, state = city_tup

    #name -> __init__(n)
    #pop -> __init__(p)
    #state -> __init__(s)
    #city is instance of the City class
    #city -> product City -> factory
    city = City(name,pop,state)
    print(city)
