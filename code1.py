
def removeDuplicate(self,nums):
    if not nums:
        return 0
    
    k=1 # initilaize the count of unique elements to 1
for i in range(1, len(nums)):
    if nums[i]!=nums[i-1]:
        nums[k]=nums[i] 
        
        k+=1
return k
    