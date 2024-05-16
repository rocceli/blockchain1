class Block:
    """
    Block: a unit of storage in a container that stores transaction.
    """
    def __init__(self, height, blockSize, blockHeader,txCount, txs):
        self.height = height
        self.blockSize = blockSize
        self.blockHeader = blockHeader
        self.txCount = txCount
        self.txs = txs