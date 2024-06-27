import CPU
import Memory
cpu = CPU.CPU()

memory_util = Memory.MemoryUtil(cpu.memory)
memory_util.writeMemoryFromBin(0x0F)

cpu.run()
#DEBUG VIEW
i = 0
ii = ""
addr = 0
maxv = 50 
start = False
for x in cpu.memory.memory_array:
    if start == False:
        print(ii)
        ii = "["+str(hex(addr))+ "]"
        i = 0
        start = True
    if i < 16:
        ii = ii + str(hex(cpu.memory.memory_array[addr])) + "|"
        i=i+1
        addr = addr + 1
    else:
        print(ii)
        ii = "["+str(hex(addr))+ "]"
        i = 0
    if addr >= maxv:
        break