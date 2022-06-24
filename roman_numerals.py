class roman_numeral:
    def __init__(self, number):
        self.number = number

    def tostring(self):
        result=''
        remainder = self.number
        dictionary ={                                       1000: "M",
                      900: "MC",    500:"D",    400:"CD",   100:"C",
                      90: "XC",     50: "L",    40:"XL",    10:"X",
                      9: "IX",      5:"V",      4:"IV",     1:"I"}


        for key in dictionary:
            while remainder>=key:
                result = result + dictionary[key]
                remainder -=key

        return result


