"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
class Car(Vehicle):
    def set_engine(self, engine_obj):
        self.engine = engine_obj



"""- в модуле `car` создайте класс `Car`
    - класс `Car` должен быть наследником `Vehicle`
    - добавьте атрибут `engine` классу `Car`
    - объявите метод `set_engine`, который принимает в себя экземпляр объекта `Engine` и устанавливает на текущий экземпляр `Car`"""