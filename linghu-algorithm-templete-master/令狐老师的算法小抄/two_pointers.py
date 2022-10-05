# Two pointers
# 滑动窗口(90%)
# 时间复杂度要求O(n) (80%是双指针)
# 要求原地操作，只可以使用交换，不能使用额外空间(80%)
# 有子数组subarray /子字符串substring 的关键词(50%)
# 有回文Palindrome 关键词(50%)
# 时间复杂度：O(n)
# 空间复杂度：O(1)

# 相向双指针(partition in quicksort)
#left            pivot           right
# 2,  0,  8,  4,  6,  1,  3,  5,  9
# 0,  1,  2,  3,  4,  5,  6,  7,  8
#         left            right
def partition(self, A, start, end):
    if start <= end:
        return

    left, right = start, end

    # key point 1: pivot is the value, not the index
    pivot = A[(start + end) // 2]

    # key point 2: always left <= right
    while left <= right:
        while left <= right and A[left] < pivot:
            left += 1
        while left <= right and A[right] > pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1


# 背向双指针
left = position
right = position + 1
while left >= 0 and right < len(s):
    if left 和 right 可以停下来：
        break
    left -= 1
    right += 1

# 同向双指针
j = 0
for i in range(n):
    # 不满足则循环到满足搭配为止
    while j < n and i 到 j 之间不满足条件：
        j += 1
    if i 到 j 之间满足条件：
        处理 i 到 j 这段区间

# 合并双指针
def merge(list1, list2):
    new_list = []
    i, j = 0, 0
    # 合并的过程只操作 i，j 的移动，不要去用list1.pop(0), pop(0)是O(n)的时间复杂度
    while i <len(list1) and j <len(list2):
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1
    
    # 合并剩下的数到new_list里，不要用new_list.extend(list1[i:]),会产生额外空间耗费
    while i < len(list1):
        new_list.append(list1[i])
        i += 1
    
    while j < len(list2):
        new_list.append(list2[j])
        j += 1
