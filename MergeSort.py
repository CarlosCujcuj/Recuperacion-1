file = open('test.txt', 'r')
file =  file.read()
text = file.split(',')



def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]


        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        l=0


        while i < len(lefthalf) and j < len(righthalf):
            guar1 = lefthalf[i]
            guar2 = righthalf[j]

            if ord(guar1[l]) == ord(guar2[l]):
                l += 1

            elif ord(guar1[l]) < ord(guar2[l]):
                alist[k] = lefthalf[i]
                i += 1

            else:
                alist[k] = righthalf[j]
                j += 1

            l = 0
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


mergeSort(text)
print(text)
