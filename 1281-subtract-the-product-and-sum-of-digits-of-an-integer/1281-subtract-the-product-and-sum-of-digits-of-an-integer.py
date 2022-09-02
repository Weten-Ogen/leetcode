class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        sam = 0
        number_string = str(n)
        array = []
        result = 0
        for i in number_string:
            mul *= int(i)
            sam += int(i)
        result = mul - sam
        return result
            
        
        