import csv


class Item:
    all_items = []

    def __init__(self, name: str, price: float, quantity=0):
        # validation
        assert price >= 0, f'Price {price} is not greater than or equal to zero.'
        assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero.'

        # Assign attributes to each instances
        self.__name = name
        self.__price = price
        self.__quantity = quantity

        # Actions to execute
        Item.all_items.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        self.__name = new_value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_value):
        if new_value >= 0:
            self.__price = new_value
        else:
            raise Exception("The price value must be greater than or equal to zero.")

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_value):
        if new_value >= 0:
            self.__quantity = new_value
        else:
            raise Exception("The quantity value must be greater than or equal to zero.")

    def total_price(self):
        return self.__price * self.__quantity

    def apply_discount(self, percent):
        self.__price -= self.__price * percent

    def increment_price(self, percent):
        self.__price += self.__price * percent

    @classmethod
    def instantiate_from_csv(cls):
        with open('db.csv', 'r') as db:
            reader = csv.DictReader(db)
            items_list = list(reader)

            for item in items_list:
                Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity'))
                )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.__name}", {self.__price}, {self.__quantity})'
