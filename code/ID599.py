class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        minn = len(list1) + len(list2)
        result = []
        for i in range(len(list1)):
            if(list1[i] in list2):
                temp = i + list2.index(list1[i])
                if(temp < minn):
                    minn = temp
                    result = [list1[i]]
                elif(temp == minn):
                    result.append(list1[i])
        return result
                    