class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        temp = []
        for i in range(len(ops)):
            if(ops[i] != "D" and ops[i] != "C" and ops[i] != "+"):
                temp.append(int(ops[i]))
            elif(ops[i] == "D"):
                temp.append(temp[-1]*2)
            elif(ops[i] == "+"):
                if(len(temp) == 1):
                    temp.append(temp[-1] + bk)
                else:
                    temp.append(temp[-1] + temp[-2])
            else:
                bk = temp.pop()
        return sum(temp)