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
                if "=" in self.expression[i]:
                    temp_arr.append([self.expression[i][0],self.expression[i][2]])
        self.variables = {temp_arr[i][0]:float(temp_arr[i][1]) for i in range(len(temp_arr))}

        print(self.variables)
    def operations(self,operator,a,b):
        operation = [a*b, a/b, a+b, a-b, a**b]
        operators = ['*','/','+','-','^']
        operation_dict = {operators[i]:operation[i] for i in range(len(operators))}
        print('operation dict',operation_dict)
        if operator in operation_dict:
            return operation_dict.get(operator)
    def count_expression(self):
        for el in self.expression:
            print(el)
            if ("\t" not in el) and ("def" not in el) and ("=" not in el):
                temp_v=[]
                for k in el:
                    if k in self.variables.keys():
                        temp_v.append(self.variables.get(k))
                    elif k.isdigit():
                        temp_v.append(float(k))
                print(temp_v)
                print(self.operations(el[1],temp_v[0],temp_v[1]))
    

a = Expression()
a.reading('expression.txt')
a.init_var()
a.count_expression()