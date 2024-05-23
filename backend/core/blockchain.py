import sys
import os

# Adjust the sys.path to include the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..', 'blockchain1'))
sys.path.append(project_root)

# Import the required modules
from backend.core.blockHeader import blockHeader
from backend.core.block import Block
from backend.core.util.util import hash256
from backend.core.database.database import blockChaindb
import time

ZERO_HASH = "0" * 64
VERSION = 1

class blockchain:
    def __init__(self):
        self.createGenesisBlock()

    def writeonDisk(self,block):
        db = blockChaindb()
        db.write(block)

    def fetch_last_block(self):
        blockchaindb = blockChaindb()
        return blockchaindb.lastBlock()
    
    def createGenesisBlock(self):
        blockHeight = 0
        prevBlockhash = ZERO_HASH
        self.addBlock(blockHeight, prevBlockhash)
    
    def addBlock(self, blockHeight, prevBlockHash):
        timeStamp = int(time.time())
        transactions = f"codies sent {blockHeight} coins to me"
        markleRoot = hash256(transactions.encode()).hex()
        bits = "ffff001b"
        header = blockHeader(VERSION, prevBlockHash, markleRoot, timeStamp, bits)  # Renamed from blockHeader to header
        header.mine()
        self.writeonDisk([Block(blockHeight, 1, header.__dict__, 1, transactions).__dict__])
    
    def main(self):
        while True:
            lastBlock = self.fetch_last_block()
            if lastBlock:
                # Ensure lastBlock is in expected dictionary format
                if isinstance(lastBlock, dict) and "blockHeader" in lastBlock:
                    blockHeight = lastBlock.get("height", 0) + 1
                    previousblockHash = lastBlock["blockHeader"]["blockhash"]
                    self.addBlock(blockHeight, previousblockHash)
                else:
                    print("Empty or unexpected data format returned by fetch_last_block()")
                    break
            else:
                print("Failed to fetch the last block.")
                break

        

if __name__ == "__main__":
    blockchain = blockchain()
    blockchain.main()
