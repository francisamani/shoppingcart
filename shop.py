# Francis Oludhe
# Object Oriented Programming Trial

class shop:
    def __init__(self, item, value, total):
        self.item = item
        self.value = value
        self.total = total

item_1 = shop('Tea Bags', 150, 45)
item_2 = shop('Apple', 55, 12)
item_3 = shop('Family Bread', 50, 40)
item_4 = shop('Maryland', 140, 8)
item_5 = shop('Indomnie', 30, 30)

print (item_1.item, 'cost', item_1.value, 'bob each')
print (item_2.item, 'costs', item_2.value, 'bob each')
print (item_3.item, 'costs', item_3.value, 'bob each')
print (item_4.item, 'costs', item_4.value, 'bob each')
print (item_5.item, 'costs', item_5.value, 'bob each')

