import re

#getting the text the file "two cities"
text = open("two_cities.txt",encoding='utf-8').read().replace('\n','')  
num = len(text) #finding the length of the text

#deleting anything but letters and spaces(" ")
i = 0
while i < (num):
    if (not((text[i] == " ") or (re.match("^[A-Za-zΑ-Ωα-ωίϊΐόάέύϋΰήώ]*$",text[i])))): 
        text = text.replace(text[i], "")
        num = len(text) #redeclaring the total length of the text
    i += 1

#finding the length of the text without " "
j = 0
for i in range(num):
    if (not(text[i] == " ")):
        j += 1

#declaring the new text 
new_text = [" "]*j

#filling the new text 
j = 0
for i in range(num):
    if (not(text[i] == " ")):
        new_text[j] = text[i]
        j += 1

#creating a list were each itemis one character
text_list = []
text_list[:] = new_text

#convering the items of the list to their ascii values
for i in range (j):
    text_list[i] = ord(text_list[i])

#finding the length of the list withe just the odd numbers
k = 0
for i in range (j):
    if not((text_list[i] % 2) == 0) :
        k += 1

#declaring the list with the odd numbers
odd_numbers = [" "]*k

#filling the list
k = 0
for i in range (j):
    if not((text_list[i] % 2) == 0) :
        odd_numbers[k] = text_list[i]
        k += 1

#sorting the list (ascending)
odd_numbers.sort()

#declaring variables
letter = " "
percent = 0
length = len(odd_numbers)

#checking for the percentage amount of each letter
while length > 0:   #while the list odd_numbers is not empty
    #redeclaring the variables for each loop
    total = 1
    i = 1
    while i < length:   #while index i is in range
        if ((odd_numbers[0] == odd_numbers[i]) or (abs(odd_numbers[0] - odd_numbers[i]) == 32)):  #if the items are the same or their difference is 32(they are the same letter one in upper and one on lower case)
            total += 1
            del odd_numbers[i]
            length = len(odd_numbers)
            i -= 1 #reseting the index i
        i += 1
    percent = int((total/k)*100) + 1  #rounding up to the nearest integer
    letter = (chr(odd_numbers[0])).upper()  #converting the ascii number to it's corresponding leeter
    print(letter + ":" + "*"*percent)  #creating the percentage bar with *
    del odd_numbers[0]  
    length = len(odd_numbers)