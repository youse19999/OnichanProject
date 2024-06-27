class Register:
    def __init__(self,cpu):
        #General purpose register
        self.cpu = cpu
        self.regiter_array = [0]*11
        #Address register R9
        #ALU Y R10
    def set(self,dest,value):
        self.regiter_array[dest] = value
    def get(self,dest):
        return self.regiter_array[dest]