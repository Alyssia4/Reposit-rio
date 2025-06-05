import math 
class retangulo:
    def __init__(self, b, h):
        if b <= 0 or h <=0: raise ValueError()
        self._base = b
        self._altura = h 
    def set_base(self, b):
        if b <= 0: raise ValueError()
        self.__base
    def get_base(self, b):
        return 