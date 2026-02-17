class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def merge(l,r,m,arr):
            L,R = arr[l:m+1], arr[m+1:r+1]

            i,j,k = l,0,0

            while(j<len(L) and k <len(R)):
                if L[j] <= R[k]:
                    arr[i] = L[j]
                    j+=1
                else:
                    arr[i] = R[k]
                    k += 1 
                i += 1 
            while(j<len(L)):
                arr[i] = L[j]
                j += 1 
                i += 1
            while(k<len(R)):
                arr[i] = R[k]
                k += 1 
                i += 1

        def mergeSort(arr, l, r):
            if l>= r:
                return 
            
            m = l + (r-l)//2

            mergeSort(arr,l,m)
            mergeSort(arr,m+1, r)
            merge(l,r,m,arr)

        mergeSort(nums, 0, len(nums)-1)
        return nums