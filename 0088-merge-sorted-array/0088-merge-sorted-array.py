class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insert=len(nums1)-1

        while m-1>=0 and n-1>=0:
            if nums1[m-1]>nums2[n-1]:
                nums1[insert]=nums1[m-1]
                m-=1
            else:
                nums1[insert]=nums2[n-1]
                n-=1
            insert-=1
        while n-1>=0:
            nums1[insert]=nums2[n-1]
            n-=1
            insert-=1
        


         