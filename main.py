#-*- coding: utf-8 -*-

from tkinter import *
from random import randint

root = Tk()
root.title("słówka")
root.geometry("800x600")

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

word_file = "slowka.txt" # path or file with words

class ReadFile():
    def __init__(self):
        opened_file = open(word_file, "r", encoding="utf-8")

        self.slowka = {}
        
        # for single_word in opened_file:
        #     self.slowka[(single_word.split("-")[0]).strip()] = (single_word.split("-")[1]).strip() old way of handling word files
        
        for line in opened_file.readlines():
            is_Definition = False
            is_Commented = False #if the word is commented with "#" that means it shall be not put in the word bank
            definition_word = ""
            meaning_words = []
            word = ""
            for letter in line:
                if letter in "-" and not is_Definition:
                    is_Definition = True
                    word = self.CheckAndRemoveLastSpace(word) # chop off the last character of a word if it is a space
                    definition_word = word
                    word = ""

                elif letter in "/\n" and is_Definition:
                    word = self.CheckAndRemoveLastSpace(word) # chop off the last character of a word if it is a space
                    meaning_words.append(word)
                    word = ""
                elif letter in "#":
                    is_Commented = True
                    word = ""
                    break
                else:
                    word += letter

            if not is_Commented:
                for meaning_word in meaning_words:
                    self.slowka[definition_word] = meaning_word.strip()
            else:
                is_Commented

        opened_file.close()
    
    def CheckAndRemoveLastSpace(self, word):
        if word[-1] in " ":
            word = word[:-1]
        return word

####################################################################

class Losowanie():
    def __init__(self):
        self.__ilosc_slowek__ = len(WordBank.slowka)
        self.__dzielnik__ = int(len(WordBank.slowka) // 4)
        self.definicja = 0
        self.uzyte_slowka = []
        self.NieudaneSlowka = []
        self.__id_slowka__ = 0
        self.noweSlowko()
        
    liczbaProb = 1
        
    def getWordDefinitionById(self, id):
        return WordBank.slowka[list(WordBank.slowka)[id]]

    def getWordMeaningById(self, id):
        return list(WordBank.slowka)[id]

    def noweSlowko(self):
        while True:
            if self.czyPowtorka():
                self.__id_slowka__ = self.getZepsuteSlowko()
                # print("ID TRAFIONEGO SŁÓWKA TO:" + str(self.__id_slowka__))
                # print("A Z TEGO WYNIKA ŻE SŁÓWKO TO" + str(WordBank.slowka[list(WordBank.slowka)[self.__id_slowka__]]))
                break
            else:
                self.__id_slowka__ = randint(0, len(WordBank.slowka) - 1) #losowa
                if self.__id_slowka__ not in self.uzyte_slowka:
                    break
                # elif len(self.NieudaneSlowka) > 0:
                #     losowa = self.getZepsuteSlowko()

        if self.__id_slowka__ not in self.NieudaneSlowka:
            self.ZbanowaneSlowka(self.__id_slowka__)
        
        self.slowko = self.getWordMeaningById(self.__id_slowka__)
        self.definicja = self.getWordDefinitionById(self.__id_slowka__)

        pokaz.configure(text=self.definicja) #pokazywanie na ekranie

    def sprawdzWynik(self):
        podane_slowo = wprowadzanie.get()

        wprowadzanie.delete(0, END)
        if (podane_slowo.lower() == self.slowko.lower()): #jeżeli dobrze wpiszemy słowo

            pop_slowko.configure(text=self.slowko, foreground="green")
            wpis_slowko.configure(text="")

        else: #jeżeli źle wpiszemy słowo
            wpis_slowko.configure(text=podane_slowo)
            pop_slowko.configure(text=self.slowko, foreground="red")

            self.addZepsuteSlowko(self.__id_slowka__)

            # print(list(podane_slowo))
            # print(list(self.slowko))
        slowka_ktore_byly = Label(root, text=str(self.slowko) + " - " + str(self.definicja), font=czcionka).pack()
        

        self.noweSlowko()
        if learning:
            ilosc_slowek.configure(text="Ilość słówek to:" + str(len(self.uzyte_slowka)) + " / "+ str(self.__ilosc_slowek__))
    
    def ZbanowaneSlowka(self, slowko):
        self.uzyte_slowka.append(slowko)
        if (int(len(self.uzyte_slowka)) == int(self.__dzielnik__) + 1): #jeżeli limit słówek w banku zostanie wyczerpany to zacznie wypierdalać te słówka
            if learning != True:
                self.uzyte_slowka.pop(0)

        print("Uzyte slowa - "+ str(self.uzyte_slowka))
    
    def getZepsuteSlowko(self):
        if len(self.NieudaneSlowka) > 0:
            return self.NieudaneSlowka.pop(0)
    
    def addZepsuteSlowko(self, slowko):
        self.NieudaneSlowka.append(slowko)

    def czyPowtorka(self):
        if len(self.NieudaneSlowka) <= 0: #nie ciągnij skurwysynu słówek jak jeszcze nie ma żadnych
            return False
        elif len(self.NieudaneSlowka) > 5:
            return True
        else:
            print("Liczba prób " + str(self.liczbaProb))
            print("Zepsute słówka " + str(self.NieudaneSlowka))
            losowa = randint(0, 5)
            tries = self.liczbaProb
            # print("SZANSE NA SŁÓWKO WYNOSZĄ " + str(5//tries) + "%")
            while tries:
                if losowa == 0:
                    print("Czas na zepsute slowko!")
                    print("Zepsute słówko to: " + str(WordBank.slowka[list(WordBank.slowka)[losowa]]))
                    self.liczbaProb = 1
                    return True
                else:
                    self.liczbaProb += 1
                tries-=1
            return False

WordBank = ReadFile()
Losowansko = Losowanie()

def submitOnReturn(event):
    Losowansko.sprawdzWynik()

def killOnEsc(event):
    root.destroy()

baton = Button(root, text="dymy dymy", command=Losowansko.sprawdzWynik)
root.bind("<Return>", submitOnReturn)
root.bind("<Escape>", killOnEsc)
baton.pack()


root.mainloop()

#todo napisać inaczej wordbank, żeby mozna było mieć więcej definicji i napisać warunek który umożliwi podanie
#jednej z dwóch opcji
