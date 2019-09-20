#
#Descripcion: el siguiente programa toma un arreglo de numeros enteros  de otro archivo python y los ordena mediante el algoritmo de insertionsort.
#Trabajo de : Jose Matias Gonzalez Valarezo y Ana Santos




def insertion_sort (A=[int]): 
	
	for i in range (1,len(A)):
		numero_actual=A[i]
		for j in range (i-1,0,-1):
			if A[j] > numero_actual and j>=0:
				A[j+1]=A[j]
			else:
				A[j+1]=numero_actual

				break
	return print(A)

	


with open ("test_insertion.py") as f:
	B=[int(x) for x in f]
	array=[]
	for line in f:
		array.append([int(x for x in line)])


insertion_sort(B)

#sdasdS
