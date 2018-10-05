#llamamos al documento txt que esta en la misma carpeta que el directorio donde corre python
file = open('test.txt', 'r')
file =  file.read()
text = file.split(',') #las oraciones esta separadas por comas


def mergeSort(alist):
	print('Splitting: ', alist)
	if len(alist)>1:
		mid = len(alist)//2
        	lefthalf = alist[:mid]
        	righthalf = alist[mid:]
        	mergeSort(lefthalf)
        	mergeSort(righthalf)
		#llamada a los workers que estan en otras maquinas para ordenar 		las oraciones hasta el momento con la funcion SORT()
		x = client.submit(Sort,lefthalf,righthalf,alist)
		#los workers regresan los valores 
		alist = client.gather(x)
	return alist


def Sort(izquierda,derecha, lista):
	i=0
        j=0
        k=0
        l=0
        while i < len(izquierda) and j < len(derecha):
            guar1 = izquierda[i]
            guar2 = derecha[j]
            if ord(guar1[l]) == ord(guar2[l]):
                l += 1
            elif ord(guar1[l]) < ord(guar2[l]):
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            l = 0
            k = k + 1
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
	print('Merging: ', lista)
	return lista

