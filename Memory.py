class Memory:
    def __init__(self,cpu,size):
        #General purpose register
        self.cpu = cpu
        #size分のメモリーを作る。
        self.memory_array = [0] * size
    #メモリーを書き込み
    def setMemory(self,dest,value):
        if value <= 0xFF:
            self.memory_array[dest] = value
    #メモリーを取得
    def getMemory(self,dest):
        return self.memory_array[dest]
#Winows向けのメモリーのユーティリティー
class MemoryUtil:
    def __init__(self,memory):
        self.memory = memory
    #メモリーをbinから読み込みコンピュータのメモリーに書き込み
    def writeMemoryFromBin(self,length):
        with open("memory.bin", "rb") as f:
            byte = f.read(length)
            for x in range(length):
                self.memory.setMemory(x,byte[x])