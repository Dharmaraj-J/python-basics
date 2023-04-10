class Robot:
    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print('My Name is ' + self.name)
        print('My color is '+ self.color)
        print('My weight is '+ str(self.weight))
        print('')

r1 = Robot('chity','white',40)
r2 = Robot('sofia','red',35)


# r1.introduce_self()
# r2.introduce_self()


class Person:
    def __init__(self,name,personality,is_sitting):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
         self.is_sitting = False

p1 = Person('kumar','foodie',False)
p2 = Person('siva','workaholic',True)

p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()
p2.robot_owned.introduce_self()
