class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answers = []
        for num1 in nums1:
            for num2 in nums2:
                if  num1 == num2:
                    same = False
                    for answer in answers:
                        if num1 == answer:
                            same = True                
                    if not same:
                        answers.append(num1)
        return answers