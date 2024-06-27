#OPCODE LIST
#ADD 00 DEST R0 R1
#SUB 01 DEST R0 R1
#ORR 02 DEST R0 R1
#NOR 03 DEST R0 R1
#AND 04 DEST R0 R1
#XOR 05 DEST R0 R1
#INC 06 DEST R0
#DEC 07 DEST R0
#RSH 08 DEST
#LDI 09 DEST IMMEDIATE
#JMP 10 ADDRESS
#LDR 11 DEST R9
#BIF 
class ALU:
    def __init__(self,cpu):
        self.cpu = cpu
        self.A = 0
        self.B = 0
        self.Y = 0
        self.OPCODE = 0
        self.Y = 0
        #Register or Memory
        self.RM = 0
    def run(self):
        if self.OPCODE == 0:
            Y = self.ReadRM(self.A) + self.ReadRM(self.B)
        if self.OPCODE == 1:
            Y = self.ReadRM(self.A) - self.ReadRM(self.B)
        if self.OPCODE == 2:
            Y = self.ReadRM(self.A) or self.ReadRM(self.B)
        if self.OPCODE == 3:
            Y = not (self.ReadRM(self.A) or self.ReadRM(self.B))
        if self.OPCODE == 4:
            Y = self.ReadRM(self.A) and self.ReadRM(self.B)
        if self.OPCODE == 5:
            Y = self.ReadRM(self.A) ^ self.ReadRM(self.B)
        if self.OPCODE == 6:
            Y = self.ReadRM(self.A) + 1
        if self.OPCODE == 7:
            Y = self.ReadRM(self.A) - 1
        if self.OPCODE == 8:
            pass
        if self.OPCODE == 9:
            self.WriteRM(self.A,self.B)
        if self.OPCODE == 10:
            self.cpu.register.R9 = self.A
            pass
        if self.OPCODE == 11:
            self.WriteRM(self.A,self.cpu.register.R9)
            pass
            self.cpu.register.set(10,self.Y)
    def ReadRM(self,dest):
        return self.cpu.memory.getMemory(dest)
    def WriteRM(self,dest,value):
        return self.cpu.memory.setMemory(dest,value)