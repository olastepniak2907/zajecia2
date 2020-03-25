##lista [] - wszystkie pozostałe przypadki
##krotka() - do odczytywanych wartosci
##zbiór {}- nie powtarzają się wartości
##słownik{} - indeksowanie po nazwach, do komunikacji z zewnętrznymi programami


def setup():
    size(500,500)
    stroke(0,0,255)
    strokeWeight(2)
    global natezenie
    natezenie = 0
    global index
    index = 0
    frameRate(25)
    global szerokosc
    szerokosc=200
    global wysokosc
    wysokosc=0
    
def draw():
    global natezenie
    natezenie = natezenie + 1
    if natezenie == 255:
        natezenie = 0
    line(mouseX, mouseY, width/3, height/3)
    fill(natezenie,0,0)
    rect(20,40,60,80)
    fill(0,natezenie,0)
    global szerokosc
    szerokosc = szerokosc -1
    global wysokosc 
    wysokosc = wysokosc +1
    print (wysokosc)
    if wysokosc >= 220:
        szerokosc = szerokosc + 1
        fill(natezenie,0,0)
    rect(szerokosc,wysokosc,100,100)
    
    slownik = {"czerwony":(255,0,0), "niebieski":(0,0,255), "zielony":(0,255,0)}
   # print(slownik["zielony"])
    stroke(*slownik["zielony"])
    lista = []
    global index
    for nazwa, wartosc in slownik.items():
        lista.append(wartosc)
    index +=1
    if index==3:
        index=0
    stroke(*lista[index])
    
def mousePressed():
    exit()
 
# ruch nie do końca po tym torze, który miał być
# 1,75pkt
