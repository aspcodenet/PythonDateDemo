class Konto:
    def __init__(self):
        self.Kontonummer = ""
        self.Saldo = 0

kontoLista = []


while True:
    print("1. Skapa konto")
    print("2. Lista konton")
    print("4. Ändra saldo")
    print("3. Exit")
    sel = input()
    if sel == "3":
        break
    if sel == "1":
        kontonr = input("Ange kontonummer:")
        nyaKontot = Konto()
        nyaKontot.Kontonummer = kontonr
        kontoLista.append(nyaKontot)
    if sel == "2":
        for konto in kontoLista:
            print(f"{konto.Kontonummer} - {konto.Saldo}")

    if sel == "4":
        kontonr = input("Ange kontonummer på konto som du vill ändra:")
        foundAccount = False
        for konto in kontoLista:
            if konto.Kontonummer == kontonr:
                nyttSaldo = float(input("Nytt saldo"))
                konto.Saldo = nyttSaldo
                foundAccount = True
                break
        if foundAccount == False:                
            print("Finns inte...")
                         
        





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
