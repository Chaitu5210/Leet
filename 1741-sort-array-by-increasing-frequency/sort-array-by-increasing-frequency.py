class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqnums={}
        for i in range(len(nums)):
            if nums[i] not in freqnums:
                freqnums[nums[i]]=0
            freqnums[nums[i]]+=1
        result=sorted(freqnums.items(), key=lambda x:x[1])
        finalresult=[]
        for i in range(len(result)):
            for j in range(len(result)-1):
                if result[j][1]==result[j+1][1] and result[j][0] < result[j+1][0]:
                    result[j+1],result[j]=result[j],result[j+1]

        for values in result:
            temp=[values[0]]*values[1]
            finalresult=finalresult+temp
        return finalresult