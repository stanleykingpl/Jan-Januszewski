def setup():
    size(400, 600)
    rectMode (CORNERS) # lepiej ustawić raz niż co klatkę
    
def draw():
    if mousePressed:
        rect (mouseX, mouseY, width/3*2, height/3*2)
    else:
        clear()
        
#def mousePressed():
#    clear()

#2pkt
    
