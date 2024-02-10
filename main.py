from item import Item
from phone import Phone


Item.instantiate_from_csv()
phone1 = Phone('Sony', 1000, 2, 1)
print(Item.all_items)
