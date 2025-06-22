from typing import  *

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def calc(num1, num2, ope):
            hash_map = {
                '*': 'num1 * num2',
                '+': 'num1 + num2',
                '-': 'num2 - num1',
                '/': 'num2 / num1'
            }

            return int(eval(hash_map.get(ope)))

        for x in tokens[:]:

            if x in ['/', '*', '+', '-']:
                num1 = stack.pop()
                num2 = stack.pop()
                print(num1, num2, x)
                val = calc(int(num1), int(num2), x)
                stack.append(val)
            else:
                stack.append(x)

        return stack.pop()

s=Solution()
res= s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(res)
