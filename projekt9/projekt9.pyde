def setup():

    global img
    size(1200/2, 1600/2) 

def draw():
 
    global img
    img = loadImage("cat.jpg")
    
    try:
        image(img, 50,100, 500,500) 
    except:
        print ('Nie znaleziono pliku!')
        stroke(255, 0, 0, 90)
    else:
        stroke(0, 0, 255, 90)
    finally:
        rect(20, 75, 550, 550)
        
# dziwnie reaguje dlatego, że wówczas znajduje błąd javy, a wychwytujemy dopiero ten Pythona
#1,5pkt      

    

    
