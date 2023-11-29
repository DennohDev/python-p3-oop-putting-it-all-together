class Shoe:
    def __init__(self, brand, size, condition=''):
        self._brand = brand
        self._size = size
        self.condition = condition

    def get_brand(self):
        return self._brand

    def get_size(self):
        return self._size

    def set_brand(self, brand):
        self._brand = brand

    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = 'New'
        print("Your shoe is as good as new!")

    brand = property(get_brand, set_brand)
    size = property(get_size, set_size)

    
clarks = Shoe("FiDiClarks", 9)
clarks.cobble()
print (clarks.condition)
