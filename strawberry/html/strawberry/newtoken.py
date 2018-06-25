#!/usr/bin/env python
import hashlib
hash = hashlib.sha1()
hash.update(input('enter a token: '))
hash = hash.hexdigest()
with open('tokens.txt', 'a') as tokens:
    tokens.write(hash)
    tokens.write('\n')
