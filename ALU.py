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
#ALUの実装
class ALU:
    #AとBを持つ、状態をYで返すALUです。
    def __init__(self,cpu):
        self.cpu = cpu
        self.A = 0
        self.B = 0
        self.Y = 0
        self.OPCODE = 0
        #Register or Memory
    #ALUを実行します。
    def run(self):
        #OPCODEで分岐
        if self.OPCODE == 0:
            Y = self.Read(self.A) + self.Read(self.B)
        if self.OPCODE == 1:
            Y = self.Read(self.A) - self.Read(self.B)
        if self.OPCODE == 2:
            Y = self.Read(self.A) or self.Read(self.B)
        if self.OPCODE == 3:
            Y = not (self.Read(self.A) or self.Read(self.B))
        if self.OPCODE == 4:
            Y = self.Read(self.A) and self.Read(self.B)
        if self.OPCODE == 5:
            Y = self.Read(self.A) ^ self.Read(self.B)
        if self.OPCODE == 6:
            Y = self.Read(self.A) + 1
        if self.OPCODE == 7:
            Y = self.Read(self.A) - 1
        #XORが未実装です。
        if self.OPCODE == 8:
            pass
        if self.OPCODE == 9:
            self.ReadWrite(self.A,self.B)
        if self.OPCODE == 10:
            self.cpu.register.R9 = self.A
            pass
        if self.OPCODE == 11:
            self.ReadWrite(self.A,self.cpu.register.R9)
            pass
            self.cpu.register.set(10,self.Y)
    #メモリーから読み取る。
    def Read(self,dest):
        return self.cpu.memory.getMemory(dest)
    #メモリーへ書きこむ
    def ReadWrite(self,dest,value):
        return self.cpu.memory.setMemory(dest,value)