import hashlib

def hash256(data):
    """Two rounds"""
    if isinstance(data, str):
        data = data.encode('utf-8')  # Encode Unicode string to bytes
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()
