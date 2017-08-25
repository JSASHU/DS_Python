arr = [1,10,5,6,1,0,23,50]

def merge(left, right, arr):
	
	i = 0
	j = 0
	k = 0
	
	while(i < len(left) and j < len(right)):
		if(left[i] > right[j]):
			arr[k] = left[i]
			i = i +1
		else:
			arr[k] = right[j]
			j = j +1
		k = k + 1

	while(i < len(left)):
		arr[k] = left[i]
		k = k + 1
		i = i +1
	
	while(j < len(right)): 
		arr[k] = right[j]
		k = k + 1
		j = j +1

def mergesort(arr):
	 
	if len(arr) < 2 :
		return 

	mid = len(arr)/2
	left = []
	right = []

	for k in range(0, mid):
		left.append(arr[k])
	for j in range(mid, len(arr)):
		right.append(arr[j])

	mergesort(left)
	mergesort(right)
	merge(left, right, arr)

mergesort(arr)

# Problem find max total of any four element in Array
#print arr[1]+arr[2]+arr[3]+arr[4],arr[0]+arr[1]+arr[2]+arr[3]

# Birthday cake problem
def birthdayCakeCandles(n ,arr):
    count = 1 
    for i in range(0,len(arr)-1):
        if arr[i] == arr[i-1]:
            count = count + 1
        else:
            break
    return count

result = birthdayCakeCandles(n, arr)

print(result)