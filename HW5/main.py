"""Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
    - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
    нужно использовать методы get и set"""


class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.age = age
        self.__gender = gender

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


class LonelyPerson(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.animals = dict()
        self.count_of_animals = 0

    def take_animal(self, type_of_animal, name):
        self.count_of_animals += 1
        self.animals[self.count_of_animals][type_of_animal] = name



class MarriedPerson(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.married_on = None


class Child(MarriedPerson):
    def __init__(self, name, age, gender, mother, father):
        super().__init__(name, age, gender)
        self.mother = mother
        self.father = father


Mary = MarriedPerson('Mary', 30, 'female')
John = MarriedPerson('John', 34, 'male')
Mary.married_on = John
John.married_on = Mary

Jim = Child('Jim', 6, 'male', Mary, John)

print(Jim.mother.get_name())
print(Jim.mother.married_on.get_name())

Mark = LonelyPerson('Mark', 15, 'male')
Mark.take_animal('cat', 'Lionel')
Mark.take_animal('dog', 'Biorn')

print(Mark.animals)