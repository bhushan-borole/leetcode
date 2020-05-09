class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        arr2 = arr.copy()
        i = 0
        j = 0
        while i < len(arr):
            if not arr2[j]:
                arr[i] = 0
                i += 1
                if i < len(arr):
                    arr[i] = 0
            else:
                arr[i] = arr2[j]
            j += 1
            i += 1
