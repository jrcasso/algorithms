class Solution:
    mapping = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
    def myAtoi(self, str: str) -> int:
        trimmed_string = str.lstrip()
        container = []
        result = 0

        try:
            if trimmed_string[0] == '-':
                trimmed_string = trimmed_string[1:]
                sign = -1
            elif trimmed_string[0] == '+':
                trimmed_string = trimmed_string[1:]
                sign = 1
            else:
                sign = 1
        except IndexError:
            return 0
            
        for i in range(len(trimmed_string)):
            try:
                container.insert(0, self.mapping[trimmed_string[i]])
            except KeyError:
                if len(container) > 0:
                    break
                return 0

        for i in range(len(container)):
            try:
                result += sign * container[i] * (10 ** i)
            
                if result >= 2147483647 or result <= -2147483648:
                    raise OverflowError
            except OverflowError:
                if sign == 1:
                    return 2147483647
                else:
                    return -2147483648
        
        return result
