import hashlib

def hash256(data):
    """Two rounds"""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()