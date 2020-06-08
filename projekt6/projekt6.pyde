class Kwadrat():
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class WypelnionyKwadrat(Kwadrat):
    def sketchWypelniony(self):
        Kwadrat.sketch(self, x, y)
    def sketchWypelniony(self, x, y, kolory):
         Kwadrat.sketch(self, x, y)
         fill(random(255), 205, 5)
         rect(self.x, self.y, self.bok, self.bok)
    
def setup():
    size(600, 600)
    malyWypelnionyKwadrat = WypelnionyKwadrat(50.0) 
    malyWypelnionyKwadrat.sketchWypelniony(random(255), 125, 5) 
    malyWypelnionyKwadrat.sketchWypelniony(random(150),268, 7) 
    duzyWypelnionyKwadrat = WypelnionyKwadrat(140.0)
    duzyWypelnionyKwadrat.sketchWypelniony(random(300), 36, 15)
    duzyWypelnionyKwadrat.sketch(random(250), 300) 
