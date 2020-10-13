def findmax(arr, light):
    for i in range(len(light)):
        print light[i]
        arr.remove(light[i])
    return max(arr)

nums = [5, 4, 3, 2, 1]

reward = ["Gold Medal", "Silver Medal", "Bronze Medal"]
for i in range(4, len(nums)+1):
    reward.append(str(i))
    
light = []

for i in range(len(nums)):
    ind = nums.index(findmax(nums, light))
    nums[ind] = reward[i]
    light.append(reward[i])
print nums