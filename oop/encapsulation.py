class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def _get_age(self):
        return self._age
    
    