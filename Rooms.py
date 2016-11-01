#Author: Ásgeir Örn Sigurpálsson
#Date: 29 oct 2015
#Type: MessyBessy - Room Scheduling
#Input: stofur.csv
#Output: rooms.dat
#   Makes the dat file rooms.dat which includes rooms, room capacity, computer rooms, special rooms, buildings,
#rooms in each buildings and room priority.
#how the doctument looks like:
#Bygging	Stofa	Sætafjöldi	Tegund	Tölvuver	Forgangur	Forgangssvið

import os, csv
from collections import OrderedDict
_trans = str.maketrans('ÁÐÉÍÓÚÝÞÆÖáðéíóúýþæö_  ','ADEIOUYTAOadeiouytao_ -')
_wenc = 'utf_8'

DI = [{} for i in range(6)]
DII = [{} for i in range(6)]
with open('stofur.csv',"r",encoding='latin-1', newline='') as csvfile:

    RoomData = csv.reader(csvfile, delimiter=';')
    next(RoomData)
    for rows in RoomData:
        for i in range(6):
            DI[i][rows[1]] = rows[i+1]
            print(DI[1])



with open('rooms.dat','w', encoding=_wenc) as fdat:


#Must be updated - computer rooms should not be in this list
    s='set Rooms:='
    fdat.write(s)
    fdat.write('\n')
    for rooms,cap in DI[2].items():
        if cap =='Almenn':
            fdat.write(rooms.translate(_trans))
            fdat.write('\n')
    fdat.write(';\n')
    fdat.write('\n')


    s='param RoomCapacity:='
    fdat.write(s)
    fdat.write('\n')
    for room,cap in DI[1].items():
        fdat.write(room.translate(_trans)+' '+cap)
        fdat.write('\n')
    fdat.write(';\n')
    fdat.write('\n')

    s='set ComputerRooms:='
    fdat.write(s)
    fdat.write('\n')
    for room,com in DI[3].items():
        if com =='Já':
            fdat.write(room.translate(_trans))
            fdat.write('\n')
    fdat.write(';\n')
    fdat.write('\n')

    s='set SpecialRooms:='
    fdat.write(s)
    fdat.write('\n')
    for room,com in DI[2].items():
        if com =='Sér':
            fdat.write(room.translate(_trans))
            fdat.write('\n')
    fdat.write(';\n')
    fdat.write('\n')

    s='param RoomPriority:='
    fdat.write(s)
    fdat.write('\n')
    for room, pri in DI[4].items():
        fdat.write(room.translate(_trans)+' '+pri)
        fdat.write('\n')
    fdat.write(';\n')
    fdat.write('\n')


#/*
#ID number for buildings
#Adalbygging	1
#Askja	2
#Arnagardur	3
#Eirberg	4
#Gimli	5
#Haskolatorg	6
#Logberg	7
#Oddi	8
#VRII	9
#Hamar	10
#Klettur	11
#Enni	12
#Laugarvatn	13
#Nýji Garður 14
#*/

#Part made manually..Must be made differently.

    s='set Building:=1 2 3 4 5 6 7 8 9 10 11 12 13 14;'
    fdat.write(s)
    fdat.write('\n\n')

    s='set RoomInBuilding[1] := A050 A051 A052 A069 A207 A218 A222 A225 A229; \n'
    fdat.write(s)
    s='set RoomInBuilding[2] := Askja130 Askja131 Askja;\n'
    fdat.write(s)
    s='set RoomInBuilding[3] := A201 A301 A303 A304 A310 A311 A101; \n'
    fdat.write(s)
    s='set RoomInBuilding[4] := E101C E201C E203C E205C E103C; \n'
    fdat.write(s)
    s='set RoomInBuilding[5] := G101; \n'
    fdat.write(s)
    s='set RoomInBuilding[6] := HT102 HT103 HT104 HT105 HT204 HT300 HT301 HT302 HT315; \n'
    fdat.write(s)
    s='set RoomInBuilding[7] := L102 L103 L201 L204 L205;\n'
    fdat.write(s)
    s='set RoomInBuilding[8] := O102 O103 O201 O202 O301; \n'
    fdat.write(s)
    s='set RoomInBuilding[9] := V138 V147 V152 V156 V258 V260 V261;\n'
    fdat.write(s)
    s='set RoomInBuilding[10] := H101 H201 H202 H203 H204 H205 H206 H207 H208 H209;\n'
    fdat.write(s)
    s='set RoomInBuilding[11] := K204 K205 K206 K207 K208;\n'
    fdat.write(s)
    s='set RoomInBuilding[12] := E301 E303;\n'
    fdat.write(s)
    s='set RoomInBuilding[13] := K-salur K-salur_b Stofa_2;\n'
    fdat.write(s)
    s='set RoomInBuilding[14] := NG014 NG015;\n\n'
    fdat.write(s)

    s='end;\n'
    fdat.write(s)
    fdat.write('\n')
