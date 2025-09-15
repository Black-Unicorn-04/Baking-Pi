from item import Item

class Phone(Item): #inheriting from Item
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0): #magic methods

        #call to super function to have access to all attributes/methods
        super().__init__(
            name, price, quantity
        )
        #Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} for {name} is not greater or equal to zero!"

        #Assign to self object

        self.broken_phones = broken_phones 