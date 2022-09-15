def selectionSort(items):
    for i in range(len(items) - 1):
        smallest = i
        print(items)
        for j in range(i + 1, len(items)):
            if items[smallest] > items[j]:
                smallest = j
            items[smallest], items[i] = items[i], items[smallest]

    return items


items = [7, 4, 9, 2, 3]

print(selectionSort(items))
