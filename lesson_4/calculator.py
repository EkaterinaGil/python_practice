class Calculator:

    def sum(self, a, b):
        return a + b
    
    def div(self, a, b):
        if (b == 0):
            raise ArithmeticError('нельзя делить на ноль')
        else:
            return a / b
        
    def mul(self, a, b):
        return a * b    
    
    def sub(self, a, b):
        return a - b
    
    def avg(self, arr):
        len_of_arr = len(arr)
        if len_of_arr == 0:
            return 0
        sum = 0
        for x in arr:
            sum += x
        avg = self.div(sum, len_of_arr)
        return avg    