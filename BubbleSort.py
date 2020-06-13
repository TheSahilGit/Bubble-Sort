"""Bubble sort core algorithm."""
### Sahil Islam ###
### 13/06/2020 ###


def oneDSort(List):
    print("Unsorted: " + str(List))
    count = 0
    for i in range(len(List)):
        for j in range(len(List) - 1):
            if List[j] > List[j + 1]:
                List[j], List[j + 1] = List[j + 1], List[j]
                count = count + 1

    print("Sorted: " + str(List) + "\n No of swaps(Bubble Sort)= " + str(count))
    return List


def twoDSort(List):
    print("Unsorted: " + str(List))
    countx = 0
    county = 0
    for p in range(len(List)):
        for q in range(len(List) - 1):
            for r in range(len(List)):
                if List[r, q] > List[r, q + 1]:
                    List[r, q], List[r, q + 1] = List[r, q + 1], List[r, q]
                    countx = countx + 1

    for j in range(len(List)):
        for k in range(len(List) - 1):
            for l in range(len(List)):
                if List[k, l] > List[k + 1, l]:
                    List[k, l], List[k + 1, l] = List[k + 1, l], List[k, l]
                    county = county + 1

    print("Sorted: " + str(List) + "\nSwaps(Bubble Sort)= " + "(" + str(countx) + "," + str(county) + ")")
    return List
