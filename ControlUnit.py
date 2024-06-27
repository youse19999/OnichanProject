class ControlUnit():
    def __init__(self,cpu):
        self.cpu = cpu
    def next(self):
        #0x00,LDI 0x16 0xFF
        #0x08 0x16 0xFF
        #fetch
        op = [0,0,0]
        self.cpu.alu.OPCODE = self.python1BytesToInt(self.readBytes(1))
        self.cpu.alu.A = self.python4BytesToInt(self.readBytes(4))
        self.cpu.alu.B = self.python4BytesToInt(self.readBytes(4))
        self.cpu.alu.run()
    def readBytes(self,length):
        i = b""
        for x in range(length):
            i = i + bytes([self.cpu.memory.getMemory(self.cpu.register.get(9))])
            self.cpu.register.set(9,self.cpu.register.get(9)+1)
        return i
    def python1BytesToInt(self,value):
        return int.from_bytes(b"\x00\x00\x00"+value)
    def python4BytesToInt(self,value):
        return int.from_bytes(value)