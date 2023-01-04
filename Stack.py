# push: lägg data på stacken
# pop: ta bort senast inlagda data och returnera det 
# peek: returnera senaste inlgda data men ta inte bort det
# is_empty: returnera True om stacken är tom
# make_empty: töm stacken
# print_stack: skriv ut innehållet i stacken


class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        popped = self.stack.pop()
        return popped
    
    def peek(self):
        element = self.stack[-1]
        return element
    
    def print_stack(self):
        for i in self.stack[::-1]:
            print(i)
        # count = -1
        # for i in self.stack:
        #     print(self.stack[count])
        #     count -= 1
    

