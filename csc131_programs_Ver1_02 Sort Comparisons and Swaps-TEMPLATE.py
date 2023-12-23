######################################################################################################################
# Name: Satyendra Raj Singh
# Date: 12/12/2023
# Description: Sort,Comparisions, and Swaps of given list in 4 types of shorting
######################################################################################################################

# creates the list
def getList():
	return [100, 5, 63, 29, 69, 74, 96, 80, 82, 12]
#	return [82, 65, 93, 0, 60, 31, 99, 90, 31, 70]
#	return [63, 16, 78, 69, 36, 36, 3, 66, 75, 100]
#	return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#	return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#	return [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]

# the bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def bubble(list):
	n = len(list)
	comparisons = 0
	swaps = 0
	for i in range(1, n):
		for j in range(1, n-i+1):
			comparisons += 1
			if (list[j] < list[j-1]):
				swaps += 1
				temp = list[j]
				list[j] = list[j-1]
				list[j-1] = temp
		
	return list, comparisons, swaps

# the optimized bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def optimized(bub):
    n = len(bub)
    comparisons = 0
    swaps = 0
    for i in range(n - 1):
        update= False 
        for j in range(n - i - 1):
            comparisons += 1
            if bub[j] > bub[j + 1]:  
                swaps += 1
                bub[j], bub[j + 1] = bub[j + 1], bub[j]
                update = True
        if not update:
            break
    return bub, comparisons, swaps


# the selection sort function
# input: a list of integers
# output: a number of comparisons and swaps
def selection(sel):
        n = len(sel)
        comparisons = 0
        swaps = 0
        for i in range(0, n-1):
                minPosition = i
                for j in range(i+1, n):
                        comparisons +=1
                        if(sel[j] < sel[minPosition]):
                                minPosition = j
                                
                temp = sel[i]
                sel[i] = sel[minPosition]
                sel[minPosition] = temp
                swaps += 1
        return sel, comparisons, swaps

# the insertion sort function
# input: a list of integers
# output: a number of comparisons and swaps
def insert(list1):
        comparisions = 0
        swaps = 0
        n = len(list1)
        i = 1
        while(i<n):
                if (list1[i-1] > list1[i]):
                        temp = list1[i]
                        j = i-1
                        while (j >= 0 and list1[j] > temp):
                                comparisions +=1
                                list1[j+1] = list1[j]
                                j-=1
                                swaps +=1
                        comparisions +=1
                        list1[j+1] = temp
                        i += 1
        return list1, comparisions, swaps
                

# the main part of the program
original_list = getList()
print(f"The List: {original_list}")
counts = bubble(original_list)
print("sorted list using bubble sort:", counts[0])
print(f"Number of comparsions: {counts[1]} and swaps: {counts[2]}")

original_list = getList()
print("The list:", original_list)
sortedlist = optimized(original_list)
print("sorted list using optimized bubble sort:", sortedlist[0])
print(f"Number of comparisions: {sortedlist[1]} and swaps: {sortedlist[2]}")




original_list = getList()
print(f"The List: {original_list}")
selects = selection(original_list)
print("sorted list using selection sort:", selects[0])
print(f"Number of comparisions: {selects[1]} and swaps: {selects[2]}")

original_list = getList()
print(f"The List: {original_list}")
in1 = insert(original_list)
print("sorted list using insertaion sort:", in1[0])
print(f"Number of comparisions: {in1[1]} and swaps: {in1[2]}")
