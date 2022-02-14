class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        # IMPORTANT
        #__init__ return None not anything else

    def sort_priority(self):
        return self.price

L = [
    Fruit('Cherry',10),
    Fruit('Apple',5),
    Fruit('Blueberry',20)
]

for f in sorted(L, key=Fruit.sort_priority):
    print(f.name)
