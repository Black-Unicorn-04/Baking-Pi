import csv

class Item:
    pay_rate = 0.8 #The pay rate after 20% discount # a class attribute
    all = []
    def __init__(self, name: str, price: float, quantity=0): #magic methods
        #Run validations to the received arguments
        assert price >= 0, f"Price {price} for {name} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} for {name} is not greater or equal to zero!"

        #Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self) #appends the instances

    @property
    #Property decoratoe = Read-only attribute
    def name(self):
        # print ("You are trying to get a name")
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value




    def calculate_total_price(self): #creating a method
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    #making it a class method
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'), 
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )  

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point  zero.
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            #The next line counts out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self): 
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
   

    def connect(self, smpt_server):
        pass

    def prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times

        Regards, B.U.
        """
    def send(self):
        pass
    
    def send_email(self):
        self.connect()
        self.prepare_body()
        self.send()
