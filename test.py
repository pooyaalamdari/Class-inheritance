current_year = 2022
class Person:
    def __init__(self, name, born):
        self.name = name
        self.born = born

    def getAge(self):
        return current_year - self.born

    def __str__(self):
        return f'{self.name} : {self.getAge()}'

#want to build new class thas has all Person class
#features plus new own feature

class Student(Person):
    def __init__(self, name, born):
        Person.__init__(self, name, born)
        self.knowledge = 0

    #def getAge applied from Person
    #def __str__ applied from Person

    def study(self):
        self.knowledge += 1

john = Student('John Doe', 1996)
john.study()
print(john.knowledge)

#if we don't call knowledge it automate runs Person class
print(john)
