from datetime import datetime, timedelta

julAfton = datetime(2021,12,24)
idag =  datetime.now()
timespan = julAfton - idag
print(f"Det är {timespan.days} dagar")

invoiceDate = datetime.now()
forFalloDag =  invoiceDate +  timedelta(days=32)
print(forFalloDag.weekday())
if forFalloDag.weekday() == 5:
    forFalloDag = forFalloDag - timedelta(days=1)
if forFalloDag.weekday() == 6:
    forFalloDag = forFalloDag + timedelta(days=1)

formattedInvoiceDate = invoiceDate.strftime('%Y-%m-%d')
print(f"Fakturadatum: {formattedInvoiceDate}")
formattedForFalloDag = forFalloDag.strftime('%Y-%m-%d')
print(f"Förfallodag: {formattedForFalloDag}")

while True:
    print("Skriv in din födelsedag - ex 1972-08-03:")
    datum = input()
    dat = datetime.strptime(datum, "%Y-%m-%d" )
    print(f"Du är född på en {dat.weekday()}")

precisNu = datetime.now()
#print(precisNu)

#snyggTid = f"{precisNu.year}-{precisNu.month}-{precisNu.day}"
snyggTid = precisNu.strftime("%Y-%m-%d")
print(snyggTid)



ettAnnat = datetime(1972,8,3)


jagArFoddDettaDatum = datetime(1972,8,3)
print(jagArFoddDettaDatum.weekday() )

weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

print(weekDays[3])
print(weekDays[jagArFoddDettaDatum.weekday()])


lista = [12,22,33]
dc = { "Namn":"Kalle", "Adress":"Hejgatan12"}
print(dc['Namn'])

idag = datetime.now()

if idag.day != 1:
    print("Kör batch")

print(idag.year)
print(idag.month)
print(idag.day)
#DEBUG OCH SE. Hmmm
# i denna "låda" idag ligger
# det massa delar inte som lista/dictionary
#utan på ett tredje sätt. What???
#Hello OOP ;)
print(idag)