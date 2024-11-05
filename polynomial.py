import copy
from matrix import SquareMatrix

class Monomial:
    def __init__(self, k, power):
        self.k = k
        self.power = power

    def __lt__(self, other):
        return self.power > other.power
    
    @staticmethod
    def multiply(left, right):
        return Monomial(left.k * right.k, left.power + right.power)
    
    @staticmethod
    def transform_horizontally(monomial, delta):
        if monomial.power == 0:
            return Polynomial.const_polynomial(monomial.k)
        
        transformed = Polynomial([Monomial(1, 1), Monomial(delta, 0)])
        transformed = Polynomial.raise_to_a_power(transformed, monomial.power)
        transformed = Polynomial.multiply(transformed, Polynomial([Monomial(monomial.k, 0)]))
        return transformed

class Polynomial:
    elements = list()

    def size(self):
        return len(self.elements)


    def first_element(self):
        if self.size() > 0:
            return self.elements[0]
        else:
            return None
    
    def add_el(self, element):
        self.elements.append(element)

    def __init__(self, elements=list()):
        self.elements = list()
        for el in elements:
            self.elements.append(Monomial(el.k, el.power))

    def __str__(self):
        self.simplify()
        flag = False
        for el in self.elements:
            if el.k != 0:
                flag = True
        if not flag:
            return "0"
        rslt = ""
        for i in range(self.size()):
            el = self.elements[i]
            rslt += f"{el.k}x^{el.power} + "
        return rslt[:-3]

    def simplify(self):
        self.elements = sorted(self.elements)

        new_elements = list()
        prev = self.elements[0]
        for i in range(1, len(self.elements)):
            current = self.elements[i]
            if prev.power == current.power:
                prev.k += current.k
            else:
                new_elements.append(Monomial(prev.k, prev.power))
                prev = current
        new_elements.append(Monomial(prev.k, prev.power))
        self.elements = new_elements

    def is_const(self):
        return self.size() == 1 and self.elements[0].power == 0
    
    def value(self, n):
        self.simplify()
        sum = 0
        for el in self.elements:
            sum += el.k * (n ** el.power)
        return sum
    
    def matrix_value(self, matrix):
        self.simplify()
        rslt = SquareMatrix(matrix.n, 0)
        for el in self.elements:
            current = copy.deepcopy(matrix)
            current = SquareMatrix.multiply_by_a_number(SquareMatrix.raise_to_a_power(current, el.power), el.k)
            rslt = SquareMatrix.add(rslt, current)
        return rslt
        
    @staticmethod
    def zero_polynomial():
        return Polynomial([Monomial(0, 0)])
    
    @staticmethod
    def const_polynomial(c=1):
        return Polynomial([Monomial(c, 0)])
    
    @staticmethod
    def opposite_polynomial(polynom):
        rslt = copy.deepcopy(polynom)
        for i in range(rslt.size()):
            rslt.elements[i].k *= -1
        return rslt

    @staticmethod
    def add(left, right):
        rslt = copy.deepcopy(left)
        for el in right.elements:
            rslt.elements.append(el)
        return rslt
    
    @staticmethod
    def add_const(polynom, n):
        return Polynomial.add(polynom, Polynomial.const_polynomial(n))
    
    @staticmethod
    def substract_const(polynom, n):
        return Polynomial.add(polynom, Polynomial.const_polynomial(-1 * n))

    @staticmethod
    def substract(left, right):
        return Polynomial.add(left, Polynomial.opposite_polynomial(right))

    @staticmethod
    def multiply(left, right):
        rslt = list()
        for left_el in right.elements:
            for right_el in left.elements:
                rslt.append(Monomial.multiply(left_el, right_el))

        return Polynomial(rslt)
    
    @staticmethod
    def multiply_by_const(polynom, n):
        return Polynomial.multiply(polynom, Polynomial.const_polynomial(n))

    @staticmethod
    def raise_to_a_power(polynom, n):
        rslt = copy.deepcopy(polynom)
        for i in range(1, n):
            rslt = Polynomial.multiply(rslt, polynom)
        return rslt
    
    @staticmethod
    def transform_horizontally(polynom, delta):
        transformed = []
        for el in polynom.elements:
            transformed.append(Monomial.transform_horizontally(el, delta))
        rslt = Polynomial([])
        for el in transformed:
            rslt = Polynomial.add(rslt, el)
        return rslt
    
    @staticmethod
    def transform_vertically(polynom, k):
        rslt = copy.deepcopy(polynom)
        for i in range(rslt.size()):
            rslt.elements[i].k *= (k ** rslt.elements[i].power)
        return rslt