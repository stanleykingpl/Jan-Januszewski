global cWidth
global cHeight
cWidth = 900
cHeight = 900
class player(object):
    def __init__(self):
        self.x = 1000
        self.y = 1000
        self.up = 0
        self.down = 0
        self.left = 0
        self.right= 0
        self.speed= 8
        self.h = 90
        self.w = 60
    def show(self):
        fill(random(255), 30, 130)
        rect(self.x,self.y,self.w,self.h)
    def update(self):
        self.x = self.x + (self.right - self.left)*self.speed
        self.y = self.y + (self.down - self.up)*self.speed
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
    global p
    p = player()
    
def draw():
    background(0, 230, 0)
    p.show()
    p.update()
    
def keyPressed():
    if keyCode == UP:
        p.up=1
    if keyCode == DOWN:
        p.down=1
    if keyCode == LEFT:
        p.left=1
    if keyCode == RIGHT:
        p.right=1
        
def keyReleased():
    if keyCode == UP:
        p.up=0
    if keyCode == DOWN:
        p.down=0
    if keyCode == LEFT:
        p.left=0
    if keyCode == RIGHT:
        p.right=0
