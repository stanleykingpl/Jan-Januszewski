from abc import ABCMeta, abstractmethod 
class Pet():
    __metaclass__=ABCMeta
    @abstractmethod 
    def speak(self): 
        super().__init__()
        return 'no sound'

class Wolf(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('auuuu', random(50, width-70), random(50, height-50))
        return 'auuuu'
    def gimmePaw(self):
        image(loadImage("wilku.png"), random(50, width-70), random(50, height-50))
    def __add__(self, other):
        return self.name[0]+ ' i ' + other.name[0]
class Bunny(Pet):
    pass

class Fox(Pet):
     def __init__(self, name):
        self.name = name
     def speak(self):
        text('wrrrrr', random(50, width-70), random(50, height-50))
        return 'wrrrrr'
  
def setup():
    size(600,600)
    textSize(20)
    Borewicz = Wolf('Borewicz')
    Rudy = Fox('Rudy')
    global list_of_pets
    list_of_pets = [Borewicz, Rudy] 
    print(isinstance(Borewicz, Pet))
    print(Borewicz+Rudy)
   
def draw(): 
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak()
        if isinstance(pet, Wolf): 
            pet.gimmePaw()
