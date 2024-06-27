class Memory:
    def __init__(self,cpu,size):
        #General purpose register
        self.cpu = cpu
        self.memory_array = [0] * size
    def setMemory(self,dest,value):
        if value <= 0xFF:
            self.memory_array[dest] = value
    def getMemory(self,dest):
        return self.memory_array[dest]
class MemoryUtil:
    def __init__(self,memory):
        self.memory = memory
    def writeMemoryFromBin(self,length):
        with open("memory.bin", "rb") as f:
            byte = f.read(length)
            for x in range(length):
                self.memory.setMemory(x,byte[x])