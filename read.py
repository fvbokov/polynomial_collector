from polynomial import Polynomial, Monomial

def read_element(input, negative=False):
    coef = 0
    power = 0
    if 'x' in input:
            if '^' in input:
                coef = int(input.split('x')[0] if input.split('x')[0] != "" else 1)
                power = int(input.split('x')[1][1:])
            else:
                if input == 'x':
                    coef = 1
                    power = 1
                elif input == '-x':
                    coef = -1
                    power = 1
                else:
                    coef = int(input.split('x')[0])
                    power = 1
    else:
        coef = int(input)
    return Monomial(coef if negative == False else coef * -1, power)

def read_polynomial(input):
    elements = []
    data = input.split()

    elements.append(read_element(data[0]))

    for i in range(1, len(data), 2):
        negative = data[i] != "+"
        elements.append(read_element(data[i + 1], negative))
        
    return Polynomial(elements)