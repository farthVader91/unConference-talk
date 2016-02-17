#! /usr/bin/env python
from hashlib import sha1

SIZE_128_MB = 131072
BIG_FILE_PATH = 'big_file'

def file_chunker(file_path, chunk_size=SIZE_128_MB):
    with open(file_path, 'rb') as big_file:
        for chunk in iter(lambda: big_file.read(chunk_size), ''):
            yield chunk

def get_sha1_hash(file_path):
    hash_obj = sha1()
    for chunk in file_chunker(file_path):
        hash_obj.update(chunk)
    return hash_obj.hexdigest()

if __name__ == '__main__':
    file_hash = get_sha1_hash(BIG_FILE_PATH)
    print file_hash
