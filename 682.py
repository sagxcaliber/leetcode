class Solution:
    def calPoints(self, operations) -> int:
        my_stack = []
        for x in operations:
            if x in ['C','D','+']:
                if x == '+':
                    my_stack.append(my_stack[-1] + my_stack[-2])
                elif x=='D':
                    my_stack.append(my_stack[-1]*2)
                elif x == 'C' and len(my_stack)>0:
                    my_stack.pop()
            else:
                my_stack.append(int(x))
        
        return  sum(my_stack)
        
s = Solution()

print(s.calPoints(["5","2","C","D","+"]))