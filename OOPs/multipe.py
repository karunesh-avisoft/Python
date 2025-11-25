class Father:
    def skills(self):
        print('Analytical', 'Calm', 'Rigid')
        
class Mother:
    def skills(self):
        print('Talktive','Emotional')
        
class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        return "Over Thinker"

child1=Child()

print(child1.skills())