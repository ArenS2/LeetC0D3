class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = []
        for i in range(len(numbers)):
            if(temp.count(numbers[i]) < 2):
                temp.append(numbers[i])
        
        for i in range(len(temp)):
            check = 0
            for j in range(i+1, len(temp)):
                if(temp[i] + temp[j] == target):
                    re = [temp[i], temp[j]]
                    check = 1
                    break
            if(check == 1):
                break
                    
        a1 = numbers.index(temp[i]) + 1
        a2 = numbers[a1:].index(temp[j]) + 1 + a1
        return [a1, a2]
                