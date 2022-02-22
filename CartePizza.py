from logging import exception
from xmlrpc.client import boolean

class CartePizzeriaException (Exception):
    pass

class CartePizzeria :
    def __init__(self, pizzas=[]):
        self.__pizzas = pizzas
        
    @property
    def pizzas(self):
        return self.__pizzas
    @pizzas.setter
    def pizzas(self, value):
        self.__pizzas = value
    
    def is_empty(self,pizzas):
      return not pizzas
      
    def  nb_pizzas(self) :
        return len(self.pizzas)
    def add_pizza(self) :
        self.add(self.pizzas)
        
    def remove_pizza(self):
        try :
            self.remove(self.pizzas)
        except ValueError:
            raise CartePizzeriaException("pizza not exist")
            

  