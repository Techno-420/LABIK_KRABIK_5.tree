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
        self.variables = {temp_arr[i][0]:temp_arr[i][1] for i in range(len(temp_arr))}

        print(self.variables)
    def count_expression(self):
        None
a = Expression()
a.reading('expression.txt')
a.init_var()