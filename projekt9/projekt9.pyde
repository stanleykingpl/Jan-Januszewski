def setup():

    global img
    size(1200/2, 1600/2) 

def draw():
 
    global img
    img = loadImage("cat.jpg")

    image(img, 50,100, 500,500) 

    try:
 
        f = open("cat.jpg")
        if f.name == 'cat.jpg':
            raise Exception
            
            
            

    
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print ('Nie znaleziono pliku!')
        rect(20, 75, 550, 550)
        fill (255, 0, 0, 90)
    
    else:
        rect(20, 75, 550, 550)
        fill (0, 0, 255, 90)
        
        
        #nie rozumiem dlaczego wyświetla się błąd, że FileNotFoundError jest niezdefiniowany, a gdy zrobimy jakąś najmniejszą edycje np. enter po jakiejś linijce i nie zapiszemy zmian, to działa. Po zapisaniu zmian znowu nie działa

               

    

    
