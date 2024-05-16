import sys
sys.path.append('/home/rocceli/projects')

from backend.core.blockHeader import blockHeader
from backend.core.block import Block
from backend.core.util.util import hash256
import time

ZERO_HASH = "0" * 64
VERSION = 1

class blockchain:
    def __init__(self):
        self.chain = []
        self.createGenesisBlock()
    
    def createGenesisBlock(self):
        blockHeight = 0
        prevBlockhash = ZERO_HASH
        self.addBlock(blockHeight,prevBlockhash)
    
    def addBlock(self,blockHeight,prevBlockHash):
        timeStamp = int(time.time())
        transactions = f"codies transaction sent{blockHeight}"
        markleRoot = hash256(transactions.encode()).hex()
        bits = "ffff001b"
        blockHeader = blockHeader(VERSION,prevBlockHash,markleRoot,timeStamp,bits)
        blockHeader.mine()
        self.chain.append(Block(blockHeight,1,blockHeader,1,transactions))
        print(self.chain)

if __name__ == "__main__":
    blockchain = blockchain()