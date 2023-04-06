#!/usr/bin/env python3
import ipdb

class Shoe:
    def __init__(self, brand="brand", size=0, material="material", condition="condition"):
        self.brand = brand
        self.size = size
        self.material = material
        self.condition = condition

    def get_size(self):
        return self._size

    def set_size(self, size):
        if (type(size) == int):
            self._size = size
        else:
            print("size must be an integer")
        
    size = property(get_size, set_size)

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

ipdb.set_trace()

