from backend.core.util.util import hash256
class blockHeader:
    def __init__(self,version,previousBlockhash,markleRoot,timestamp,bits,nonce):
        self.version = version
        self.previousBlockhash = previousBlockhash
        self.markleRoot = markleRoot
        self.timestamp = timestamp
        self.bits = bits
        self.nonce = 0
        self.blockhash=""

    def mine(self):
        while(self.blockhash[0:4]!="0000"):
            self.blockhash=hash256(str(self.version)+self.previousBlockhash+self.markleRoot+str(self.timestamp)+str(self.bits)+str(self.nonce)).hex()
            self.nonce+=1
            print("Mining started {self.nonce}", end="\r")