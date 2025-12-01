class Father:
    def skills(self):
        print('In fathers mehtod.')
        print('Analytical', 'Calm', 'Rigid')
        
class Mother:
    def skills(self):
        print('In mothers mehtod.')
        print('Talktive','Emotional')
        
class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print('In childs.')
        return "Over Thinker"

child1=Child()

print(child1.skills())
# method resolution order (mro)
print(Child.__mro__)
print(Child.mro())