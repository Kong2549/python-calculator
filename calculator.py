class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        is_negative = False
        
        if b < 0:
            is_negative = True
            b = -b
            
        for i in range(b):
            result = self.add(result, a)
            
        if is_negative:
            return -result
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
            
        is_negative = (a < 0) ^ (b < 0)
        a, b = abs(a), abs(b)
        
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
            
        if is_negative:
            return -result
        return result
    
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero.")
            
        a, b = abs(a), abs(b)
        while a >= b:
            a = self.subtract(a, b)
        return a
