class HomeAnimal(object):
    future_food = True
    life_interval = 0
    position = 0
    name = ''
    speed = 0   # km/h
    appearance = ''
    flying = False

    def __init__(self, future_food, life_interval, position, name, speed, appearance, flying):
        self.future_food = future_food
        self.life_interval = life_interval
        self.position = position
        self.name = name
        self.speed = speed
        self.appearance = appearance
        self.flying = flying

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
    pass


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


def main():
    all = dict(
        duck=Duck(True, 3, 0, 'e2e4', 0, '', True),
        chicken=Chicken(True, 2, 0, 'coco', 0, '', False),
        geese=Geese(True, 3, 0, 'gaga', 0, '', False),
        pig=Pig(True, 5, 0, 'MrPig', 0, '', False),
        sheep=Sheep(True, 6, 0, 'MisSheep', 0, '', False),
        goats=Goats(True, 6, 0, 'MisGoats', 0, '', False),
        cow=Cow(True, 5, 0, 'Muuu', 0, '', False),
    )
    for val in all.values():
        print(str(val))


if __name__ == "__main__":
    main()
