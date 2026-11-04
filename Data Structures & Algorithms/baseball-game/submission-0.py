class Solution:
    def calPoints(self, operations: List[str]) -> int:
        

        list = []

        for op in operations:

            if op == "+":
                b = list.pop()
                a = list.pop()
                c = int(a) + int(b)
                list.append(a)
                list.append(b)
                list.append(c)
            elif op == "D":
                b = list.pop()
               
                c = 2*int(b)
                
                list.append(b)
                list.append(c)
            elif op == "C":
                list.pop()
            else:
                list.append(op)

        sum = 0
        for x in list:
            sum += int(x)

        return sum