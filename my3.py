import math

class TestVector(object):
    def __init__(self, dimension, values):
        try:
            self.dimension = int(dimension)
        except:
            self.dimension = 1
            dimension = 1
        i = 0
        self.values = []
        for i in range(dimension):
            try:
                self.values.append(float(values[i]))
            except:
                self.values.append(0)

    def len(self):
        a = 0
        for i in range(0, self.dimension):
            a += self.values[i] ** 2
        a = math.sqrt(a)
        return a

    def get_value(self, position):
        value = 0;
        try:
            value = self.values[position - 1]
        except Exception:
            #print("WroOOong!!!")
            return None
        else:
            return value

    def __str__(self):
        ans_str = '[ '
        for i in range(0, self.dimension):
            ans_str += " " + str(self.values[i]) + " "
            if i != self.dimension - 1:
                ans_str += ";"
        return ans_str + "]"

    def __add__(self, other):
       if self.dimension == other.dimension:
           v = TestVector(self.dimension, [])
           for i in range(0, self.dimension):
               v.values[i] += self.values[i] + other.values[i]
           return v

    def __sub__(self, other):
       if self.dimension == other.dimension:
           v = TestVector(self.dimension, [])
           for i in range(0, self.dimension):
               v.values[i] += self.values[i] - other.values[i]
           return v

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            v = TestVector(self.dimension, [])
            for i in range(0, self.dimension):
                v.values[i] += other * self.values[i]
            return v
        else:
            if self.dimension == other.dimension:
                v = TestVector(self.dimension, [])
                for i in range(0, self.dimension):
                   v.values[i] += self.values[i] * other.values[i]
                return v

    def __eq__(self, other):
        ans = self.len() == other.len()
        return ans
    def __ne__(self, other):
        ans = self.len() != other.len()
        return ans
    def __lt__(self, other):
        ans = self.len() < other.len()
        return ans
    def __le__(self, other):
        ans = self.len() <= other.len()
        return ans
    def __gt__(self, other):
        ans = self.len() > other.len()
        return ans
    def __ge__(self, other):
        ans = self.len() >= other.len()
        return ans

def ShowWork(a, b, c):
    string_ans = ''

    string_ans += str(a) + '\n'
    string_ans += str(b) + '\n'
    string_ans += str(c) + '\n'
    
    string_ans += '\nДлины векторов:' + '\n'
    string_ans += str(a.len()) + '\n'
    string_ans += str(b.len()) + '\n'
    string_ans += str(c.len()) + '\n'

    string_ans += '\nПолучение 3 значения:' + '\n'
    string_ans += str(a.get_value(3)) + '\n'
    string_ans += str(b.get_value(3)) + '\n'
    string_ans += str(c.get_value(3)) + '\n'

    string_ans += '\nСумма 2 векторов:' + '\n'
    d = a + b
    string_ans += str(a) + ' + ' + str(b) + ' = ' + str(d) + '\n'
    d = a + c
    string_ans += str(a) + ' + ' + str(c) + ' = ' + str(d) + '\n'

    string_ans += '\nРазность 2 векторов:' + '\n'
    d = a - b
    string_ans += str(a) + ' - ' + str(b) + ' = ' + str(d) + '\n'

    string_ans += '\nПроизведение 2 векторов:' + '\n'
    d = a * b
    string_ans += str(a) + ' * ' + str(b) + ' = ' + str(d) + '\n'

    string_ans += '\nСравнение 2 векторов:' + '\n'
    ans = a == b
    string_ans += str(a) + ' == ' + str(b) + ' = ' + str(ans) + '\n'
    ans = a > b
    string_ans += str(a) + ' > ' + str(b) + ' = ' + str(ans) + '\n'
    ans = a < b
    string_ans += str(a) + ' < ' + str(b) + ' = ' + str(ans)

    return string_ans

#print(ShowWork(TestVector(3, [5, 6, 7]), TestVector(3, [12, 0, 4]), TestVector(2, [4, 5])))
