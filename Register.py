#R1~R8は汎用
#R9は制御装置の位置のレジスター
#R10はALUはALUの結果用のレジスター
class Register:
    def __init__(self,cpu):
        #General purpose register
        self.cpu = cpu
        self.regiter_array = [0]*11
        #Address register R9
        #ALU Y R10
    #レジスターへの書き込み
    def set(self,dest,value):
        self.regiter_array[dest] = value
    #レジスターからの取得
    def get(self,dest):
        return self.regiter_array[dest]