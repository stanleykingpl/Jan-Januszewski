add_library("pdf")

def setup():
    global img
    global i
    size(198, 255)#, PDF, "mojPDF.pdf")
    beginRecord(PDF, "mojPDF.pdf")
    img=loadImage("dowodowe.jpg")
    imageMode(CENTER)
    image(img, width/2, height/2)
    
def draw():
    global img
    global i
    if (mousePressed == True):
        i = loadImage("oksy.png")
        image(i, width/2, 135, 140, 70)
        endRecord()
