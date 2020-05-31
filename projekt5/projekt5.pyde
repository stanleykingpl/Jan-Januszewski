global cWidth
global cHeight
cWidth = 900
cHeight = 900
class Player(object): # nazwy klas piszemy dużą literą
    up = False
    down = False
    left = False
    right= False # tam gdzie są tylko dwie opcje lepiej używać typu logicznego niż liczbowego
    def __init__(self, x, y): # dzięki przekazaniu przez argumenty mogą być różne dla różnych instancji
        self.x = x
        self.y = y
        self.speed= 8
        self.h = 90
        self.w = 60
    def show(self):
        fill(random(255), 30, 130)
        rect(self.x,self.y,self.w,self.h)
    def update(self):
        self.x = self.x + (Player.right - Player.left)*self.speed
        self.y = self.y + (Player.down - Player.up)*self.speed
        if not (self.x >= 0):
            self.x = 0
        if not (self.x <= (cWidth - self.w)):
            self.x = (cWidth - self.w)
        if not (self.y >= 0):
            self.y = 0
        if not (self.y <= (cHeight - self.h)):
            self.y = (cHeight - self.h)


def setup():
    size(cWidth,cHeight)
    global p1, p2
    p1 = Player(1000,1000)
    p2 = Player(100,100) # miały być dwa obiekty klasy
    
def draw():
    background(0, 230, 0)
    p1.show()
    p1.update()
    p2.show()
    p2.update()
    
def keyPressed():
    if keyCode == UP:
        Player.up=1 # dzięi temu, że to atrybuty klasy, a nie obiektu, ustawiamy dla wszystkich obiektów wspólnie
    if keyCode == DOWN:
        Player.down=1
    if keyCode == LEFT:
        Player.left=1
    if keyCode == RIGHT:
        Player.right=1
        
def keyReleased():
    if keyCode == UP:
        Player.up=0
    if keyCode == DOWN:
        Player.down=0
    if keyCode == LEFT:
        Player.left=0
    if keyCode == RIGHT:
        Player.right=0
        
# 1,5pkt
