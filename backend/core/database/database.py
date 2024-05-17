import os
import json

class baseDB:
    def __init__(self):
        self.basepath= "data"
        self.filepath= "/".join((self.basepath, self.filename))

    def read(self):
        if not os.path.exists(self.filepath):
            print("File does not exist")
            return False
        with open(self.filepath, "r") as f:
            raw = f.readline()
        if len(raw) > 0:
            data = json.loads(raw)
        else:
            data = []
        return data

    def write(self, data):
        item = self.read()
        if item:
            item = item + data
        else:
            item = data
        with open(self.filepath, "w+") as f:
            f.write(json.dumps(item))

class blockChaindb(baseDB):
    def __init__(self):
        self.filename = "blockchain"
        super().__init__()

    def lastBlock(self):
        data = self.read()
        if data:
            return data[-1]