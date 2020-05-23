class Expression:
    def __init__(self):
        self.expression = []
        self.variables = {}
        self.tree = {}

    def reading(self, name):
        expr = open(name, 'r')
        for lines in expr:
            self.expression.append(lines)
        for i in range(len(self.expression) - 1):
            self.expression[i] = self.expression[i][:-1]
        for i in range(len(self.expression)):
            self.expression[i] = self.expression[i].split(" ")
        for i in range(len(self.expression)):
            for j in range(len(self.expression[i])):
                if self.expression[i][j][:1] == "\t":
                    print(self.expression[i][j][:1])
                    self.expression[i][j] = self.expression[i][j][1:]
                    self.expression[i].insert(0, "\t")
        print(self.expression)

    def init_var(self):
        temp_arr = []
        for i in range(len(self.expression)):
            if ("=" in self.expression[i]) and ('\t' not in self.expression[i]):
                temp_arr.append([self.expression[i][0], self.expression[i][2]])
        self.variables = {temp_arr[i][0]: float(temp_arr[i][1]) for i in range(len(temp_arr))}

        print(self.variables)

    def operations(self, operator, a, b):
        operation = [a * b, a / b, a + b, a - b, a ** b]
        operators = ['*', '/', '+', '-', '^']
        operation_dict = {operators[i]: operation[i] for i in range(len(operators))}
        if operator in operation_dict:
            return operation_dict.get(operator)

    def parse_tree(self):
        temp_str = ' '
        for el in self.expression:
            if ("\t" not in el) and ("def" not in el) and ("=" not in el):
                temp_str = temp_str.join(el)
                self.tree = {temp_str: el for i in range(len(el))}
                print(self.tree)
        arr_items = self.tree.get(temp_str)
        self.count_expression([arr_items])

    def count_expression(self, expression):

        for el in expression:
            if len(el) > 3:
                el1 = el[:3]
                if ("\t" not in el1) and ("def" not in el1) and ("=" not in el1):
                    temp_v = []
                    for k in el:
                        if k in self.variables.keys():
                            temp_v.append(self.variables.get(k))
                        elif k not in ['*', '/', '^', '+', '-']:
                            temp_v.append(float(k))
                    el = el[3:]
                    self.variables['el1'] = self.operations(el1[1], temp_v[0], temp_v[1])
                    el.insert(0, self.variables.get('el1'))
                    self.count_expression([el])
            else:
                if ("\t" not in el) and ("def" not in el) and ("=" not in el):
                    temp_v = []
                    for k in el:
                        if k in self.variables.keys():
                            temp_v.append(self.variables.get(k))
                        elif k not in ['*', '/', '^', '+', '-']:
                            temp_v.append(float(k))
                    return self.operations(el[1], temp_v[0], temp_v[1])

    def function_reader(self):
        parameters = []
        expr = []
        var_arr = []
        for k in range(len(self.expression)):
            if 'def' in self.expression[k]:
                for el in self.expression[k]:
                    if el in self.variables.keys():
                        parameters.append(el)
            elif "return" in self.expression[k]:
                expr = self.expression[k][2:]
            elif "\t" in self.expression[k] and "return" not in self.expression[k]:
                var_arr.append(self.expression[k])
        print(expr)
        for element in var_arr:
            del element[0]
            if '=' in element:
                if len(element[2:]) is 1:
                    self.variables[element[0]] = float(element[2])
                else:
                    self.variables[element[0]] = self.count_expression([element[2:]])
        print(self.variables)
        # print("var_arr", var_arr)
        print("k", self.count_expression([expr]))



a = Expression()
a.reading('expression.txt')
a.init_var()
# a.count_expression(a.expression)
a.parse_tree()
a.function_reader()