import sys
import os

# Adjust the sys.path to include the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..', 'blockchain1'))
sys.path.append(project_root)

from backend.core.util.util import hash256
class blockHeader:
    def __init__(self,version,previousBlockhash,markleRoot,timestamp,bits):
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
            print(f"Mining started {self.nonce}", end="\r")