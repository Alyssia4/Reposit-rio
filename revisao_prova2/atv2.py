import math

class pais:
    def __init__(self, nome, população, área):
        self._nome = nome
        self._população = população
        self._área = área
    def set_nome(self, N):
        if N < 0: raise ValueError()
        self._nome = N
    def get_nome(self):
        return self._nome
    def set_população(self, P):
        if P < 0: raise ValueError()
        self._população = P
    def get_população(self):
        return self._população
    def set_área(self, A):
        if A < 0: raise ValueError()
        self._área = A