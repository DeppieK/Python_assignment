import random
import numpy as np
print ("Εισαγωγή διαστάσεων")

#getting the values from the user
height = ""
width = ""
while ((height == "") or (width == "")):
    height = input("Εισαγωγή μήκους ορθογωνίου:")
    width = input("Εισαγωγή πλάτους ορθογωνίου:")

rows = int(height) 
columns = int(width)
table_sos = np.array([" "]*rows*columns)
total_spaces = 0
total_sos = 0
repeats = 1

#importing equal amounts of s and o into a list
for i in range (int(rows*columns / 2)+1):
    table_sos[i] = "s"

for i in range ((int(rows*columns / 2)+1) , rows*columns):
    table_sos[i] = "o"

#the loop repeats for 100 times
while repeats <= 100:

    #suffle the array
    random.shuffle(table_sos)
    newtable_sos = table_sos.reshape(rows,columns)
    
    #checking for sos vertically
    for i in range (rows):
        for j in range (columns - 2):
            if (newtable_sos[i][j] + newtable_sos[i][j+1] + newtable_sos[i][j+2]) == "sos":
                total_sos += 1

    #checking for sos horizontally
    for j in range (columns):
        for i in range (rows - 2):
            if (newtable_sos[i][j] + newtable_sos[i+1][j] + newtable_sos[i+2][j]) == "sos":
                total_sos += 1

    i = 0
    #checking for sos diagonally (forward)
    while i < (rows - 2):
        for j in range (columns - 2):
            if (newtable_sos[i][j] + newtable_sos[i+1][j+1] + newtable_sos[i+2][j+2]) == "sos":
                total_sos += 1
        i += 1

    i = 0
    #checking for sos diagonally (backwards)
    while i < (rows - 2):
        for j in range (columns-1,0,-1):
            if (newtable_sos[i][j] + newtable_sos[i+1][j-1] + newtable_sos[i+2][j-2]) == "sos":
                total_sos += 1
        i += 1

    repeats += 1

#prints the average amount of sos
print("Ο μέσος όρος των τριάδων sos είναι:")
if total_sos != 0:
    print(total_sos // 100)
elif total_sos == 0:
    print("0")

