

class Item:

    def __init__(self, property_1=None, property_2=None, property_3=None,
                 property_4=None, property_5=None, property_6=None, property_7=None,
                 property_8=None, property_9=None, property_10=None, property_11=None,
                 property_12=None, property_13=None):
        self.property_1 = property_1
        self.property_2 = property_2
        self.property_3 = property_3
        self.property_4 = property_4
        self.property_5 = property_5
        self.property_6 = property_6
        self.property_7 = property_7
        self.property_8 = property_8
        self.property_9 = property_9
        self.property_10 = property_10
        self.property_11 = property_11
        self.property_12 = property_12
        self.property_13 = property_13

    def __str__(self):
        return f'You can change what you want to see in the object, ' \
                f'when you print it, say its first property: {self.property_1}'


