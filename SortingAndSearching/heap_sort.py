# link - http://quiz.geeksforgeeks.org/heap-sort/
# February 12, 2017

class HeapSort:

    def __init__(self):
        self.heap_size = None
        pass

    def parent(self, i):
        return i/2

    def left(self, i):
        return 2*i

    def right(self, i):
        return 2*i+1

    # convert the array into max heap
    def __build_max_heap(self, a):

        self.heap_size = len(a)-1
        for i in range(len(a)/2-1, -1, -1):
            self.__max_heapify(a,i)

    # arrange the array, to maintain heap property
    def __max_heapify(self,a, i):

        l = self.left(i)
        r = self.right(i)

        if l <= self.heap_size-1 and a[l] > a[i]:
            largest = l
        else:
            largest = i
        
        if r <= self.heap_size-1 and a[r] > a[largest]:
            largest = r

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            self.__max_heapify(a,largest)

    def heap_sort(self, a):

        self.__build_max_heap(a)
        for i in range(len(a)-1, 1, -1):
            a[0], a[i] = a[i], a[0]
            self.heap_size = self.heap_size-1
            self.__max_heapify(a,0)


if __name__ == "__main__":

    a = [12, 11, 13,5,8,20,54,1, 5, 6, 7]
    obj = HeapSort()
    obj.heap_sort(a)
    print a

