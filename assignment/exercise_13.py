import re

#getting the text the file "two cities"
text = open("two_cities.txt",encoding='utf-8').read().replace('\n','')

#getting the total length of the text for the loop
text_length = len(text)

#deleting anything but letters and spaces(" ")
i = 0
while i < (text_length):
    if (not((text[i] == " ") or (re.match("^[A-Za-zΑ-Ωα-ωίϊΐόάέύϋΰήώ]*$",text[i])))): 
        text = text.replace(text[i], "")
        text_length = len(text) #redeclaring the total length of the text
    i += 1

text_list = text.split(" ") #forming a list in which every item is a word from the text
total_length = 0 #the sum of every items length in the list
list_length = len(text_list) #amount of items in the list

#deleting the empty items
i = 0
while (i < list_length):
    if (text_list[i] == ""):
        del text_list[i]
        list_length = len(text_list)
    i += 1

#finding item couples with total length 20 and removing them from the list
i = 0
while (list_length != 0): #until there are no words
    hasCouples = 0
    while i < (list_length - 1):
        j = 1
        while j < (list_length - 1):
            if (len(text_list[i] + text_list[j]) == 20):
                hasCouples = 1
                del text_list[i]
                del text_list[j] 
                list_length = len(text_list)
                #break
            j += 1
        i += 1
    list_length = len(text_list)
    if (hasCouples == 0): #there are no couples left so the loop has to end
        list_length = 0
    
print(text_list)
            

