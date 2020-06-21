class Kwadrat():
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class WypelnionyKwadrat(Kwadrat):
    def sketchWypelniony(self, x, y): # po co powielać? no i nie korzystasz z tej zmiennej w ogóle w ciele tej metody, więc po co ona?
         Kwadrat.sketch(self, x, y)
         fill(random(255), 205, 5) # każda rzecz rysowana po tym kwadracie będzie miała ten koloe, warto byłoby przywracać poprzednio ustawiony na koniec
         rect(self.x, self.y, self.bok, self.bok)
    
def setup():
    size(600, 600)
    malyWypelnionyKwadrat = WypelnionyKwadrat(50.0) 
    malyWypelnionyKwadrat.sketchWypelniony(random(255), 125) 
    malyWypelnionyKwadrat.sketchWypelniony(random(150),268) 
    duzyWypelnionyKwadrat = WypelnionyKwadrat(140.0)
    duzyWypelnionyKwadrat.sketchWypelniony(random(300), 36)
    duzyWypelnionyKwadrat.sketch(random(250), 300)
    
# 1,25pkt
