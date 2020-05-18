class Expression:
    def __init__(self):
        self.expression = []
        self.variables = {}
    def reading(self,name):
        expr = open(name, 'r')
        for lines in expr:
            self.expression.append(lines)
        for i in range(len(self.expression) - 1):
            self.expression[i] = self.expression[i][:-1]
a = Expression()
a.reading('expression.txt')