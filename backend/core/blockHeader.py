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