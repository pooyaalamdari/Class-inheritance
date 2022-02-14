current_year = 2022
class Person:
    def __init__(self, name, born):
        self.name = name
        self.born = born

    def getAge(self):
        return current_year - self.born

    def __str__(self):
        return f'{self.name} : {self.getAge()}'

john = Person('John Doe', 1996)
print(john)
