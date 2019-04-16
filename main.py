# -*- coding: utf-8 -*-


def swap(heap, i, j):
    tmp = heap[i]
    heap[i] = heap[j]
    heap[j] = tmp


def heapify(heap, size, i):
    """
    堆调整
    :param heap: 堆数组
    :param size: 堆数组的有效长度
    :param i: 从索引为i的元素开始调整
    :return:
    """

    lchild_index = 2 * i + 1
    rchild_index = 2 * i + 2
    if i >= int(size / 2):
        return
    max_index = i
    if rchild_index < size and heap[max_index] < heap[rchild_index]:
        max_index = rchild_index
    if lchild_index < size and heap[max_index] < heap[lchild_index]:
        max_index = lchild_index
    if max_index != i:
        swap(heap, max_index, i)
        heapify(heap, size, max_index)


def build_heap(nums):
    """
    构建大顶堆
    :param nums:
    :return:
    """
    last_parent = int(len(nums) / 2) - 1
    for i in range(last_parent, -1, -1):
        heapify(nums, len(nums), i)


def heap_sort(nums):
    """堆排序"""
    build_heap(nums)
    for i in range(len(nums) - 1, -1, -1):
        # 0 与 0 交换
        swap(nums, 0, i)
        heapify(nums, i, 0)


if __name__ == "__main__":
    nums = [2, 5, 3, 1, 10, 4]
    heap_sort(nums)
    print(nums)



