__doc__ = """

"""

def decToBin(value):
    #without sign works!
    #return bin(value)[2:]
    if(value < 0):
        result = "1"
    else:
        result = "0"

    result = result + bin(abs(value))[2:]
    return result

def binToDec(value):
    binary = value[1:]
    binary = binary[::-1]
    decimal = 0
    p = 0
    for x in binary:
        if x == "1":
            decimal = decimal + 2**p
        p = p + 1
    if value[0] == "1":
        decimal = -decimal
    return decimal

def binToBin(value):
    binary = ""
    base = 0
    ls = []
    if "0" in value and "1" in value:
        return value
    for x in value:
        if x not in ls:
            base = base + 1
            ls.append(x)
    if base != 2:
        raise ValueError
    else:
        for x in value:
            if x == ls[0]:
                binary = binary + "1"
            else:
                binary = binary + "0"
    return binary

def eqlen(value1, value2):
    """

    """
    if len(value1) != len(value2):
        if len(value1) > len(value2):
            value2.fill(len(value1))
        else:
            value1.fill(len(value2))

class BinWord(object):
    """
    
    """
    def __init__(self, value, is_bin = False):
        if is_bin:
            self.bin = binToBin(value)
            self.dec = binToDec(self.bin)
        else:
            self.dec = int(value)   
            self.bin = decToBin(self.dec)
        #self.mod = False

    def __getattr__(self):
        return self.bin

    def __add__(self, value):
        if type(value) is int:
            new_obj = BinWord(self.dec + value)
        elif type(value) is str:
            new_obj = BinWord(value, True)
            print("new_obj\n",new_obj)
            new_obj = BinWord(new_obj.dec+self.dec)
        else:
            new_obj = BinWord(self.dec + value.dec)
        return new_obj

    def __abs__(self):
        """
        returns absolute value of variable:
        11101 -> 01101
        01101 -> 01101
        """
        # result = BinWord(mod(self.dec))
        # or
        # result.bin = "0"+self.bin[1:] #doesn't care about sign bit
        return BinWord(abs(self.dec))

    def __invert__(self):
        """
        same as ~a
        return new BinWord invert of image
        bin:
              01001
            ->10110
        dec:  calculated
        """
        result = ""
        for x in self.bin:
            if x == "1":
                result = result + "0"
            else:
                result = result + "1"
        return BinWord(result, True)

    def __neg__(self):
        """
        unary. same as a = -a
        bin:  01001
            ->11001
        dec:
              9
            =-9

        """
        if self.bin[0] == "0":
            self.bin = "1" + self.bin[1:]
        else:
            self.bin = "0" + self.bin[1:]

        return BinWord(self.bin, True)

    def __sub__(self):
        """
        same as a - b
        """
        pass


    def modificate(self, modifier = 2):
        """
        do not use it
        need to re-think

        modificates code
        11101 -> 111101
        01101 -> 001101
        """
        self.bin = self.bin[0]*modifier + self.bin[1:]
        self.modifier = True

    def __len__(self):
        return len(self.bin)

    def fill(self, lenght):
        """
        fills binary representation to given lenght

        """
        if lenght <= len(self):
            raise
        else:
            self.bin = "0"*(lenght-len(self))+self.bin

    def __repr__(self):
        """
        called in shell in cond:
            >>a
            0101
        """
        return self.bin

    def __str__(self):
        """
        called in print() and in str()
        """
        return "dec: "+str(self.dec)+", bin: "+self.bin

    def __setitem__(self, where, what):
        if what in (0, 1):
            self.bin = self.bin[:where]+str(what)+self.bin[where+1:]
        self.dec = binToDec(self.bin)

#as boolean type
    def __and__(self, value):
        """
        boolean:
            same as a & b = c
            01101
          & 01010
          = 01000
        """
        eqlen(self, value)



        pass

    def __or__(self, value):
        """
        boolean:
            same as a | b = c
            01101
          | 01010
          = 01111
        """
        pass

    def __rand__(self, value):
        """
        boolean:
            same as __and__ method <=> a & b = c
        """
        pass

    def __ror__(self, value):
        """
        boolean:
            same as __or__ method <=> a | b = c
        """
        pass

    def __xor__(self, value):
        """
        boolean:
            same as __or__ method but with another syntax
            a ^ b = c
        """
        pass

    def __rxor__(self, value):
        """
        boolean:
            same as __xor__ method
        """
        pass

#compare operators
    def __eq__(self, value):
        """
        boolean:
            same as self == value
        """
        pass

    def __ne__(self, value):
        """
        boolean:
            same as self != value
        """
        pass

    def __ge__(self, value):
        """
        boolean:
            same as self >= value
        """
        pass

    def __gt__(self, value):
        """
        boolean:
            same as self > value
        """
        pass

    def __le__(self, value):
        """
        boolean:
            same as self <= value
        """
        print("lolo")
        pass

    def __lt__(self, value):
        """
        boolean:
            same as self < value
        """
        pass

#shifts
    def __lshift__(self, value, put = '0'):
        """
        Return self<<value equal as self * pow(2, value)
        """
        return BinWord(self.dec*(2**value))

    def __rshift__(self, value, put = '0'):
        """
        Return self>>value equal as self / pow(2, value)
        """
        return BinWord(self.dec/(2**value))

    def lshift(self, value, put = "0"):
        pass

    def rshift(self, value, put = "0"):
        pass
