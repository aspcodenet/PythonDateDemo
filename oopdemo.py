class Person:
    def __init__(self):
        self.Namn = ""
        self.Gatuadress = ""
        self.Postnr = ""
        self.City = ""
    def BytAddress(self, gatuadress, postnr, city):
        self.Gatuadress = gatuadress
        self.City = city
        self.Postnr = postnr


person1 = Person()
person1.Namn = "Stefan"
person1.Gatuadress = "testgatan 12"
person1.Postnr = "11111"
person1.City = "teststad"
##### 1000 RADER senare ### 2. Uppdatera

person1.BytAddress("dsadsad sasa","332133", "dsasadas")





class House:
    def __init__(self):
        self.Color = ""
        self.NrOfWindows = 0
        self.RenovationCost  = 0

stefanHus = House()
stefanHus.Color = "Brown"
stefanHus.NrOfWindows = 10

annasHus = House()
annasHus.Color = "Gult"
annasHus.NrOfWindows = 10

print(f"Stefans hus är {stefanHus.Color}")
print(f"Annass hus är {annasHus.Color}")

stefanHus.Color = "White"
stefanHus.RenovationCost = stefanHus.RenovationCost+ 10000
print(f"Stefans hus är {stefanHus.Color}")
print(f"Annass hus är {annasHus.Color}")
