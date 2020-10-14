def time_calc(t, n):
    result = []
    for i in range(t):
        if(bin(i).count("1") == n):
            if(t==60):
                result.append(str(i).zfill(2))
            else:
                result.append(str(i))
    return result

def join_arr(arr1, arr2):
    result = []
    for i in arr1:
        for j in arr2:
            result.append(i+":"+j)
    return result
            
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if(num == 0):
            return ["0:00"]
        hour = 12
        minute = 60
        result = []
        for i in range(num+1):
                result += join_arr(time_calc(hour, i), time_calc(minute, num-i))
        return result