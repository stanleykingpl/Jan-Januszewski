def setup():
    size(400, 400)
    background(21, 76, 10)
    fill(255)
    textSize(100)
    textAlign(CENTER)
    text("J", width/2-50, height/2)
    text("J", width/2+50, height/2)
    
    s = createShape()
    s.beginShape()
    s.fill(100, 100, 100)
    s.stroke(0)
    s.vertex(width/3-100, height/3*2)
    s.vertex(width/3-100, height/3*2-50)
    s.vertex(width/2, height/3*2)
    s.vertex(width/2+50, height/3*2+100)
    s.vertex(width/2-50, height/3*2)
    s.endShape(CLOSE)
    shape(s, 25, 25)
    
def draw():
    if (mousePressed == True): # miało być na najechanie, a nie klikmnięcie myszą
        text("J", width/2-50, height/2)
        text("J", width/2+50, height/2)
        fill(58, 142, 70)
    else:
        fill(0)
        
    if keyPressed: # nie ma potrzeby powielania warunku, wszystko co pod nim wytabiwane sę liczy pod niego
        if (keyCode == LEFT): # strzałki działają też gdy nic niezaznaczone, a miały zmieniać zaznaczenie między literami, gdy któraś aktywna
            fill(125)
            text("J", width/2-50, height/2)
            fill(255)
            text("J", width/2+50, height/2)
        if (keyCode == RIGHT):
            fill(140)
            text("J", width/2+50, height/2)
            fill(255)
            text("J", width/2-50, height/2)
        fill(0)
        if key == 'j' or key == 'J':
            text("J", width/2-50, height/2)
            text("J", width/2+50, height/2)
            
# 1,25pkt

        
