def mergesort(arr):
	if len(arr)>2:
		mid=len(arr)//2
		left= arr[:mid]
		right = arr[mid:]
		
		mergesort(left)
		mergesort(right)
		
		i=j=k=0
		while i<len(left) and j<len(right):
			if left[i]<right[j]:
				arr[k] = left[i]
				i+=1
			else:
				arr[k] = right[j]
				j+=1
			k+=1
		
		while i<len(left):
			arr[k]=left[i]
			i+=1
			k+=1
		while j<len(right):
			arr[k]=right[j]
			j+=1
			k+=1
def printList(arr):
	for i in range(0,len(arr)):
		print(arr[i])

arr = [12, 11, 13, 5, 6, 7]  
print ("Given array is", end ="\n")  
printList(arr) 
mergesort(arr) 
print("Sorted array is: ", end ="\n") 
printList(arr) 
