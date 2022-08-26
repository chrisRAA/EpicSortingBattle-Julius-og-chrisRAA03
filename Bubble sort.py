import random

#sort

def bubble_sort(list1):

    # Outer loop for traverse the entire list

    for i in range(0,len(list1)-1):#Den skal starte på 0 i listen og slutte på længden af listen - 1 fordi den en liste starter på 0 og ikke på 1

        for j in range(len(list1)-1):#vælger et tal i listen

            if(list1[j]>list1[j+1]):#tjeker om tallet er størrer end det næste i listen

                temp = list1[j+1]#Sætter tallet frem hvis det næste tal er mindre

                list1[j+1] = list1[j]

                list1[j] = temp#Sætter det forrige tal tilbage

    return list1






 #Main


#Generate 500 random numbers between 1 and 100

our_list = random.sample(range(1, 100), 10)

print("unsorted list ", our_list)

bubble_sort(our_list)

print("sorted list", our_list)
