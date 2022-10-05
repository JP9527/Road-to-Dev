# sorting
# 时间复杂度：
# 快速排序(期望复杂度) ： O(nlogn)
# 归并排序(最坏复杂度) ： O(nlogn)
#
# 空间复杂度：
# 快速排序： O(1)
# 归并排序： O(n)

# quick sort
class Solution:

    def sortIntegers(self, A):
        self.quickSort(A, 0, len(A)-1)
    
    def quickSort(self, A, start, end):
        if start >= end:
            return

        left, right = start, end

        # pivot is a value not index
        pivot = A[(start+end)//2]

        # always left <= right
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)


# merge sort
class Solution2:

    def sortIntegers(self, A):
        if not A:
            return A
        temp = [0] * len(A)
        self.merge_sort(A, 0, len(A) - 1, temp)

    def merge_sort(self, A, start, end, temp):
        if start >= end:
            return
        # left half
        self.merge_sort(A, start, (start+end)//2, temp)
        # right half
        self.merge_sort(A, (start+end)//2+1, end, temp)
        self.merge(A, start, end, temp)
    
    def merge(self, A, start, end, temp):
        middle = (start+end)//2
        left_index = start
        right_index = middle + 1
        index = start

        while left_index <= middle and right_index <= end:
            if A[left_index] < A[right_index]:
                temp[index] = A[left_index]
                index += 1
                left_index += 1
            else:
                temp[index] = A[right_index]
                index += 1
                right_index += 1
        
        while left_index <= middle:
            temp[index] = A[left_index]
            index += 1
            left_index += 1
        
        while right_index <= end:
            temp[index] = A[right_index]
            index += 1
            right_index += 1
        
        for i in range(start, end+1):
            A[i] = temp[i]





        

