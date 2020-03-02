def setup():
    size(400, 600)
def draw():
    rectMode (CORNERS)
    if mousePressed:
        rect (mouseX, mouseY, width/3*2, height/3*2)
    else:
        clear()
def mousePressed():
    clear()
    
