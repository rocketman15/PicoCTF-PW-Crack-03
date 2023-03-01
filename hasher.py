#this code was written on 2/28/23 to solve the PicoCTF PW Crack 4 challenge
import hashlib
def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()
passwords = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"] 
hash = open('level3.hash.bin', 'rb').read()

for i in passwords:
        if hash_pw(i) == hash:
                print(i)