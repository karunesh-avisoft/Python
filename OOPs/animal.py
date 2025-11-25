class Animal:
    def speak(self):
        print('Make a sound!')

class Dog(Animal):
    def speak(self):
        print('Whaw whaw...')

class Cat(Animal):
    def speak(self):
        print('Meowww...')
        
class Snake(Animal):
    def speak(self):
        print('Hissss...')
        
def make_sound(animal):
    animal.speak()

dog=Dog()
cat=Cat()
snake=Snake()

make_sound(snake)
make_sound(cat)
make_sound(dog)