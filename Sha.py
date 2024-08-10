import hashlib

def calculate_sha1(data):
    sha1 = hashlib.sha1(data)
    return sha1.hexdigest()

