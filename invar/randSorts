import random 

def returnArrauOfRandom(n):
	return [random.randint(0, 10) for i in range(n)]

def insertSort(array):
    a = array
    for i in range(len(a)):
        v = a[i]
        j = i;
        while (a[j-1] > v) and (j > 0):
            a[j] = a[j-1]
            j = j - 1
        a[j] = v
    return a

def heapSort (array):

    def siftDown (parent, limit):
        item = array[parent]
        while True:
            child = (parent << 1) + 1
            if child >= limit:
                break
            if child + 1 < limit and array[child] < array[child + 1]: # !
                child += 1
            if item < array[child]:                                      # !
                array[parent] = array[child]
                parent = child
            else:
                break
        array[parent] = item
    # Тело функции heap_sort
    length = len(array)
    # Формирование первичной пирамиды
    for index in range((length >> 1) - 1, -1, -1):
        siftDown(index, length)
    # Окончательное упорядочение
    for index in range(length - 1, 0, -1):
        array[0], array[index] = array[index], array[0]
        siftDown(0, index)
    return array

if __name__ == "__main__":
	ar = returnArrauOfRandom(10)

	assert(insertSort(ar) == heapSort(ar), "something went wrong")
