def selectionSort(items):
    for i in range(len(items) - 1):#holder styr på hvilket index vi er i gang med
        smallest = i
        print(items)
        for j in range(i + 1, len(items)):#sortere og vælger næste index
            if items[smallest] > items[j]:#tjekker om i er større end det næste tal
                smallest = j
            items[smallest], items[i] = items[i], items[smallest]#bytter rundt på tallene

    return items#kører programmet igennem igen


items = [7, 4, 9, 2, 3]

print(selectionSort(items))
