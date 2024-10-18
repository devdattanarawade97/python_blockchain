import hashlib

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce  # Fix: Assign nonce before hashing
        self.hash = self.hash_block()  # Fix: Calculate hash after setting nonce

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(
            str(self.index).encode('utf-8') +
            str(self.transactions).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.nonce).encode('utf-8')  # Fix: Include nonce in hash calculation
        )
        return sha.hexdigest()

    def __repr__(self):
        return 'Block({}, {}, {}, {}, {})'.format(
            self.index,
            self.transactions,
            self.timestamp,
            self.previous_hash,
            self.hash
        )
