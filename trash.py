#-*- coding: utf-8 -*-
f = open("slowka.txt", "r+", encoding="utf-8")
siemson = []
siemson1 = []
for i in f:
    siemson.append(i.strip())

for i in siemson:
    if len(i) > 1:
        siemson1.append(i)
licznik = 0
for i in siemson1:
    if licznik < len(siemson1) - 2:
        f.write(str(str(siemson1[licznik]) + " - " + str(siemson1[licznik + 1]) + "\n"))
        licznik += 2

f.close()