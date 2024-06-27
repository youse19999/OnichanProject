import ALU
import Register
import Memory
import ControlUnit
class CPU:
    def __init__(self):
        #レジスター
        self.register = Register.Register(self)
        #ALU
        self.alu = ALU.ALU(self)
        #メモリー
        self.memory = Memory.Memory(self,2048)
        #制御装置
        self.controlunit = ControlUnit.ControlUnit(self)
    def run(self):
        #コントロールユニットに命令を読み取らせる。
        self.controlunit.next()