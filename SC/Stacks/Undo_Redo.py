class Operation:
    reverse_operator_map = {'*':'/','/':'*','+':'-','-':'+'}
    def __init__(self,num):
        self.num = num
        self.undo = []
        self.redo = []
    def printNum(self):
        print(self.num)
    def calculate(self,operand,operator,undo=False):
        match operator:
            case '+':
                self.num = self.num + operand
            case '-':
                self.num = self.num - operand
            case '*':
                self.num = self.num * operand
            case '/':
                self.num = self.num / operand
        if not undo:
            self.undo.append([operand,operator])
            self.redo = []
        return self.num

    def undo_operation(self):
        temp = self.undo.pop()
        self.calculate(temp[0],self.reverse_operator_map[temp[1]],True)
        self.redo.append(temp)

    def redo_operaation(self):
        temp = self.redo.pop()
        self.calculate(temp[0],temp[1],True)

o = Operation(10)
o.calculate(5,'+')
o.calculate(5,'+')
o.printNum()
o.undo_operation()
o.printNum()



