def twoSum(nums, target):
    for i in range(len(nums)):
        if (target-nums[i]) in nums[:i]+nums[i+1:]:
            return [i,(nums[:i]+nums[i+1:]).index(target-nums[i])+1]


#2nd Method

def twoSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic:dic[nums[i]]=[]
        dic[nums[i]].append(i)
    for i in nums:
        if (target-i) in dic:
            if (target-i)!=i:
                return dic[i]+dic[target-i]
            elif len(dic[i])!=1:
                return dic


#3rd Method

#2nd Method

def twoSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic:dic[nums[i]]=[]
        dic[nums[i]].append(i)

        if (target-nums[i]) in dic:
            if (target-nums[i])!=nums[i]:
                return dic[nums[i]]+dic[target-nums[i]]
            elif len(dic[nums[i]])!=1:
                return dic[nums[i]]