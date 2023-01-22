#-*- coding: utf-8 -*-

from tkinter import *
from random import randint

root = Tk()
root.title("słówka")
root.geometry("400x300")

czcionka = ("Calibri", 20, "bold")

pokaz = Label(root, text="XD", font=czcionka)

ilosc_slowek = Label(root, text="", font=czcionka)
rezultat = Label(root, text="", font=czcionka)
wpis_slowko = Label(root, text="", font=czcionka)
pop_slowko = Label(root, text="", font=czcionka)
wprowadzanie = Entry(root)

learning = True

pokaz.pack()
wprowadzanie.pack()
wpis_slowko.pack()
pop_slowko.pack()
if learning:
    ilosc_slowek.pack()

rezultat.pack()



class plik():
    def __init__(self):
        f = open("slowka.txt", "r", encoding="utf-8")
        self.slowka = {}
        for i in f:
            self.slowka[(i.split("-")[0]).strip()] = (i.split("-")[1]).strip()
            print(i)
        f.close()

class Losowanie():
    def __init__(self):
        self.__ilosc_slowek__ = len(App.slowka)
        self.__dzielnik__ = int(len(App.slowka) // 4)
        self.uzyte_slowka = []
        self.NieudaneSlowka = []
        self.noweSlowko()

    def noweSlowko(self):
        while True:
            losowa = randint(0, len(App.slowka) - 1) #losowa
            if losowa not in self.uzyte_slowka or len(self.uzyte_slowka) == self.__ilosc_slowek__:
                break
        self.ZbanowaneSlowka(losowa)
        
        self.slowko = list(App.slowka)[losowa]
        
        pokaz.configure(text=App.slowka[list(App.slowka)[losowa]]) #pokazywanie na ekranie

    def sprawdzWynik(self):
        podane_slowo = wprowadzanie.get()

        wprowadzanie.delete(0, END)
        if (podane_slowo.lower() == self.slowko.lower()): #jeżeli dobrze wpiszemy słowo

            pop_slowko.configure(text=self.slowko, foreground="green")
            wpis_slowko.configure(text="")

        else: #jeżeli źle wpiszemy słowo
            wpis_slowko.configure(text=podane_slowo)
            pop_slowko.configure(text=self.slowko, foreground="red")

            print(list(podane_slowo))
            print(list(self.slowko))

        self.noweSlowko()
        if learning:
            ilosc_slowek.configure(text="Ilość słówek to:" + str(len(self.uzyte_slowka)) + " / "+ str(self.__ilosc_slowek__))
    
    def ZbanowaneSlowka(self, slowko):
        self.uzyte_slowka.append(slowko)
        if (int(len(self.uzyte_slowka)) == int(self.__dzielnik__) + 1): #jeżeli limit słówek w banku zostanie wyczerpany to zacznie wypierdalać te słówka
            if learning != True:
                self.uzyte_slowka.pop(0)

        print("Uzyte slowa - "+ str(self.uzyte_slowka))
        


App = plik()
Losowansko = Losowanie()

def key_pressed(event):
    Losowansko.sprawdzWynik()

baton = Button(root, text="dymy dymy", command=Losowansko.sprawdzWynik)
root.bind("<Return>", key_pressed)
baton.pack()


root.mainloop()

