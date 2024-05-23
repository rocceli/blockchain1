import os
import sys

# Adjust the sys.path to include the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from backend.core.EllepticCurve.EllepticCurve import Sha256Point
from backend.core.util.util import hash160
import secrets

class Account:
    def create_keys(self):
        Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
        Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
        G = Sha256Point(Gx, Gy)

        private_key = secrets.randbits(256)
        uncompressedPublic_key = G * private_key
        X_point = uncompressedPublic_key.x
        Y_point = uncompressedPublic_key.y

        if Y_point % 2 == 0:
            compressedPublic_key = b'\x02' + X_point.to_bytes(32, byteorder='big')
        else:
            compressedPublic_key = b'\x03' + X_point.to_bytes(32, byteorder='big')
        
        h160 = hash160(compressedPublic_key)
        """Prefix for mainnet"""
        mainnet_prefix = b'\x00'
        address = mainnet_prefix + h160
        """Checksum"""
        checksum = hash256(address)[:4]

if __name__ == "__main__":
    acc = Account()
    acc.create_keys()
