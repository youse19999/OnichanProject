import ALU
import Register
import Memory
import ControlUnit
class CPU:
    def __init__(self):
        self.register = Register.Register(self)
        self.alu = ALU.ALU(self)
        self.memory = Memory.Memory(self,2048)
        self.controlunit = ControlUnit.ControlUnit(self)
    def run(self):
        self.controlunit.next()