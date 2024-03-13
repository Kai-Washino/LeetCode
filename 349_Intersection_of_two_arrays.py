class Solution:
    def quick_sort(self, data: List[int], left: int, right: int):
        i = left
        j = right
        pivot = data[(left + right) // 2]

        while True:            
            while data[i] < pivot:
                i = i + 1
            while data[j] > pivot:
                j = j - 1
            if i >= j:                                 
                break

            data[i], data[j] = data[j], data[i]        
            i = i + 1
            j = j - 1
        
        if left < i -1:
            self.quick_sort(data, left, j)
        if right > j + 1:
            self.quick_sort(data, i, right)
        

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        self.quick_sort(nums1, 0, len(nums1) - 1)
        self.quick_sort(nums2, 0, len(nums2) - 1)
        print(nums2)
        nums1 = list(dict.fromkeys(nums1))
        nums2 = list(dict.fromkeys(nums2))
        print(nums1)
        
        answer = []
        i = 0
        j = 0
        while True:
            if nums1[i] == nums2[j]:
                answer.append(nums1[i])
                if i + 1 < len(nums1) and j + 1 < len(nums2):
                    i = i + 1
                    j = j + 1
                else:
                    break 
            elif nums1[i] < nums2[j]:
                if(i + 1 < len(nums1)):
                    i = i + 1
                else:
                    break
            elif nums2[j] < nums1[i]:
                if(j + 1 < len(nums2)):
                    j = j + 1
                else:
                    break
        return answer