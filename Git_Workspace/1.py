class marks:
    def __init__ (self, score):
        self.score = score
    def __str__ (self):
        return str(self.score)
    def __add__ (self, other):
        return self.score + other.score
    def __sub__ (self, other):
        return self.score - other.score
    def __mul__ (self, other):
        return self.score * other.score
    def __truediv__ (self, other):
        return self.score / other.score
    def __floordiv__ (self, other):
        return self.score // other.score
    def __lt__ (self, other):
        return self.score < other.score
    def __gt__ (self, other):
        return self.score > other.score
    def __le__ (self, other):
        return self.score <= other.score
    def __ge__ (self, other):
        return self.score >= other.score
    def __eq__ (self, other):
        return self.score == other.score
    def __ne__ (self, other):
        return self.score != other.score
m = marks(90)
m1 = marks(91)
print(m)
print(m + m1)
print(m - m1)
print(m * m1)
print(m / m1)
print(m // m1)
print(m < m1)
print(m > m1)
print(m <= m1)
print(m >= m1)
print(m == m1)
print(m != m1)
