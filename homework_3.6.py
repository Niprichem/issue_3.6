class HomeAnimal(object):
    future_food = True
    life_interval = 0
    position = 0
    name = ''
    speed = 0
    appearance = ''

    def __init__(self, future_food, life_interval, position, name, speed, appearance):
        self.future_food = future_food
        self.life_interval = life_interval
        self.position = position
        self.name = name
        self.speed = speed
        self.appearance = appearance

    def __repr__(self):
        return self.name

    def get_life_interval(self):
        return self.life_interval

    def set_life_interval(self, life_interval):
        self.life_interval = life_interval

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def get_appearance(self):
        return self.appearance

    def set_appearance(self, appearance):
        self.appearance = appearance


class Animal(HomeAnimal):
    presence_horns = False

    def get_present_horns(self):
        return self.presence_horns

    def set_present_horns(self, presence_horns):
        self.presence_horns = presence_horns


class Bird(HomeAnimal):
    flying = False

    def get_flying(self):
        return self.flying

    def set_flying(self, flying):
        self.flying = flying


class Cow(Animal):
    pass


class Goats(Animal):
    pass


class Sheep(Animal):
    pass


class Pig(Animal):
    pass


class Duck(Bird):
    pass


class Chicken(Bird):
    pass


class Geese(Bird):
    pass
