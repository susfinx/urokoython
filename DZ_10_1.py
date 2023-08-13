# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, **kwargs):
        if animal_type == "Dog":
            return Dog(**kwargs)
        elif animal_type == "Cat":
            return Cat(**kwargs)
        elif animal_type == "Fish":
            return Fish(**kwargs)
        else:
            raise ValueError("Unsupported animal type")


class Animal:
    def __init__ (self, name:str, age:int, poroda:str, ves:float):
        self.name = name
        self.age = age
        self.poroda = poroda
        self.ves = ves

    def get_age (self)-> int:
        return self.age

    def get_name (self) -> str:
        return self.name

    def get_poroda (self):
        return self.poroda

    def get_ves (self):
        return self.ves

class Dog (Animal):
    def __init__(self,name:str, age:int, vid:str,poroda:str, ves:float, chemp:list=None):
        super().__init__(name, age, poroda,ves)
        self.chemp = chemp if chemp is not None else []

    def add_chemp (self, chemp_str:str):
        self.chemp.append(chemp_str)

    def get_chemp (self):
        return self.chemp


class Cat (Animal):
    def __init__(self,name:str, age:int, poroda:str, ves:float, korm:str):
        super().__init__(name, age, poroda,ves)
        self.korm = korm

    def get_corm (self):
        return self.korm

class Fish (Animal):
    def __init__(self,name:str, age:int, poroda:str, ves:float, water_salt:bool):
        super().__init__(name, age, poroda,ves)
        self.water_salt = water_salt

    def get_w_salt (self):
        return self.water_salt



if __name__=='__main__':

    animal_data = {
        "name": "Buddy",
        "age": 3,
        "vid": "Some vid",  # Вам нужно предоставить значение для "vid"
        "poroda": "Golden Retriever",
        "ves": 25.0,
        "chemp": ["Best in Show"]
    }

    animal_type = "Dog"
    animal_instance = AnimalFactory.create_animal(animal_type, **animal_data)

    print(animal_instance.get_name())
    print(animal_instance.get_chemp()) 
