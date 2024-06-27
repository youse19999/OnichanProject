#制御装置の実装
class ControlUnit():
    def __init__(self,cpu):
        self.cpu = cpu
    #次の命令を読み込む
    def next(self):
        #0x00,LDI 0x16 0xFF
        #0x08 0x16 0xFF
        #fetch
        self.cpu.alu.OPCODE = self.python1BytesToInt(self.readBytes(1))
        self.cpu.alu.A = self.python4BytesToInt(self.readBytes(4))
        self.cpu.alu.B = self.python4BytesToInt(self.readBytes(4))
        self.cpu.alu.run()
    #R9からlengtyh分だけ読み取ります。
    def readBytes(self,length):
        i = b""
        for x in range(length):
            i = i + bytes([self.cpu.memory.getMemory(self.cpu.register.get(9))])
            self.cpu.register.set(9,self.cpu.register.get(9)+1)
        return i
    #1バイト用の読み取り。整数に変換。
    def python1BytesToInt(self,value):
        return int.from_bytes(b"\x00\x00\x00"+value)
    #4バイトからの読み取り整数に変換。
    def python4BytesToInt(self,value):
        return int.from_bytes(value)